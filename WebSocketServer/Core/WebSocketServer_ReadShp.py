# coding=utf8


import socket
import hashlib
import threading
import time
import struct
from base64 import b64encode
from Utils import *


connection_list = {}
g_header_length = 0


def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


def get_data_length(msg):

    global g_code_length
    global g_header_length

    g_code_length = ord(msg[1]) & 127
    if g_code_length == 126:
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]
        g_header_length = 8
    elif g_code_length == 127:
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]
        g_header_length = 14
    else:
        g_header_length = 6
    g_code_length = int(g_code_length)
    return g_code_length


def parse_data(msg):

    global g_code_length
    g_code_length = ord(msg[1]) & 127
    if g_code_length == 126:
        g_code_length = struct.unpack('>H', str(msg[2:4]))[0]
        masks = msg[4:8]
        data = msg[8:]
    elif g_code_length == 127:
        g_code_length = struct.unpack('>Q', str(msg[2:10]))[0]
        masks = msg[10:14]
        data = msg[14:]
    else:
        masks = msg[2:6]
        data = msg[6:]

    i = 0
    raw_str = ''
    for d in data:
        raw_str += chr(ord(d) ^ ord(masks[i % 4]))
        i += 1
    return raw_str


def sendMessage(message):

    global connection_list

    for connection in connection_list.values():
        back_str = "\x81"
        # back_str.append('\x81')
        data_length = len(message)

        if data_length < 126:
            back_str += struct.pack("B", data_length)
        elif data_length <= 0xFFFF:
            back_str += struct.pack("!BH", 126, data_length)
        else:
            back_str += struct.pack("!BQ", 127, data_length)

        msg = ''
        for c in back_str:
            msg += c
        back_str = str(msg) + message
        if back_str is not None and len(back_str) > 0:
            connection.send(back_str)


def del_connection(item):
    global connection_list
    del connection_list['connection' + item]


class WebSocket(threading.Thread):

    GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

    def __init__(self, conn, index, address):
        threading.Thread.__init__(self)
        self.conn = conn
        self.index = index
        self.remote = address
        self.path = "/"
        self.buffer = ""
        self.buffer_utf8 = ""
        self.length_buffer = 0
        self.handshake = False

    def run(self):

        headers = {}

        while True:
            if self.handshake is False:
                print 'Socket %s start handshake from client %s!' % (self.index, self.remote)
                self.buffer = self.conn.recv(1024 * 5)
                if self.buffer.find('\r\n\r\n') != -1:
                    header, data = self.buffer.split('\r\n\r\n', 1)
                    for line in header.split("\r\n")[1:]:
                        key, value = line.split(": ", 1)
                        headers[key] = value

                    headers["Location"] = ("ws://%s%s" % (headers["Host"], self.path))
                    key = headers['Sec-WebSocket-Key']
                    token = b64encode(hashlib.sha1(str.encode(str(key + self.GUID))).digest())

                    handshake = "HTTP/1.1 101 Switching Protocols\r\n" \
                                "Upgrade: websocket\r\n" \
                                "Connection: Upgrade\r\n" \
                                "Sec-WebSocket-Accept: " + bytes.decode(token) + "\r\n" \
                                "WebSocket-Origin: " + str(headers["Origin"]) + "\r\n" \
                                "WebSocket-Location: " + str(headers["Location"]) + "\r\n\r\n"

                    self.conn.send(str.encode(str(handshake)))
                    self.handshake = True
                    print 'Socket %s handshake success from %s!' % (self.index, self.remote)
                    sendMessage('Welcome, client : ' + repr(self.remote) + ' !')
                    self.buffer_utf8 = ""
                    g_code_length = 0

            else:
                global g_header_length
                mm = self.conn.recv(1024 * 5)
                if len(mm) <= 0:
                    continue
                if g_code_length == 0:
                    get_data_length(mm)
                self.length_buffer += len(mm)
                self.buffer = self.buffer + mm
                if self.length_buffer - g_header_length < g_code_length:
                    continue
                else:
                    self.buffer_utf8 = parse_data(self.buffer)
                    if self.buffer_utf8 == 'quit':
                        print 'Socket client %s logout!' % repr(self.remote)
                        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                        sendMessage('%s %s say: %s' % (nowTime, repr(self.remote), ' Logout'))
                        del_connection(str(self.index))
                        self.conn.close()
                        break
                    else:
                        print 'Socket %s get msg:%s from %s!' % (self.index, self.buffer_utf8, self.remote)
                        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                        message = self.buffer_utf8
                        data = ''
                        if message:
                            import arcpy
                            data_dir = GetDataDir()
                            arcpy.env.workspace = data_dir
                            shpId = message.split(',')
                            shpFields = ["OBJECTID", "SHAPE@JSON"]
                            shp = os.path.join(data_dir, 'linkgeo.shp')
                            data += '{'
                            data += '"displayFieldName": "NAME_CHN",'
                            data += ' "fieldAliases": {"%s": "%s"},' % (shpFields[0], shpFields[0])
                            data += '"geometryType": "esriGeometryPolyline",'
                            data += '"spatialReference": {"wkid": 4326,"latestWkid": 4326},'
                            data += '"fields": [{"name": "%s","type": "esriFieldTypeOID","alias": "%s"}],' % (shpFields[0], shpFields[0])
                            data += '"features": ['
                            rowNum = len(shpId)
                            n = 1
                            with arcpy.da.SearchCursor(shp, shpFields) as cursor:
                                for sid in shpId:
                                    for row in cursor:
                                        objectid = int(row[0])
                                        if int(sid) == objectid:
                                            geo = str(row[1]).split(':')[1].split(',"')[0]
                                            data += '{'
                                            data += '"attributes": {"%s": %d},' % (shpFields[0], objectid)
                                            data += '"geometry": {"paths":%s}' % geo
                                            if n != rowNum:
                                                data += '},'
                                                n += 1
                                            else:
                                                data += '}]}'
                                            break
                            print data
                            sendMessage(data.encode('utf-8'))
                        else:
                            sendMessage('%s %s say: %s' % (nowTime, repr(self.remote), message))
                    self.buffer_utf8 = ""
                    self.buffer = ""
                    g_code_length = 0
                    self.length_buffer = 0
            self.buffer = ""


class WebSocketServer(object):
    def __init__(self):
        self.socket = None

    def begin(self):
        print('WebSocketServer Start Working !')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("192.168.2.113", 12345))
        self.socket.listen(50)

        global connection_list
        i = 0

        while True:
            connection, address = self.socket.accept()
            newSocket = WebSocket(connection, i, address)
            newSocket.start()
            connection_list['connection' + str(i)] = connection
            i += 1


if __name__ == "__main__":
    server = WebSocketServer()
    server.begin()
