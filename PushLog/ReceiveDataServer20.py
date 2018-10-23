# -*- coding: utf-8 -*-


from SocketServer import BaseRequestHandler, ThreadingTCPServer
from SendDataClient20 import *

"""
    用来接收XXXX数据流,别的机器拒接
    向 10.212.129.3 机器发送接收到数据
"""


class TCPServer(BaseRequestHandler):
    def handle(self):
        """
        覆写Handle方法
        :return：返回值为数据长度
        """
        cIP = self.client_address[0]
        cPORT = self.client_address[1]
        locIP = socket.gethostbyname(socket.gethostname())
        print '%s : %d Connect Success :' % (cIP, cPORT)
        try:
            buf = 1024 * 1024
            dataLen = self.request.recv(buf)
            if str(dataLen).isdigit():
                dataContent = self.request.recv(buf)
                if int(dataLen) == len(dataContent):
                    self.request.sendall('1')
                    print 'Receive %s : %d Data Success .' % (cIP, cPORT)
                    IP = '192.168.2.109'
                    PORT = 10253
                    sendData(IP, PORT, dataLen, dataContent)
                else:
                    print 'Data Not Correct , ReSend Me .'
                    self.request.sendall('0')

        except Exception as e:
            print 'Handle Occur Exception :' + e.message


if __name__ == '__main__':
    """
    设置IP为任意端口
    PORT为10000 + 本机末尾IP
    """
    host = ""
    port = 10020
    addR = (host, port)
    print 'Waite Connect .........'
    server = ThreadingTCPServer(addR, TCPServer)
    server.allow_reuse_address = True
    server.serve_forever()


