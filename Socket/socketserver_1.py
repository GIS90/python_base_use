# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import SocketServer
from SocketServer import StreamRequestHandler
from time import ctime

host = '192.168.1.104'
port = 9999
addr = (host, port)


class Servers(StreamRequestHandler):
    def handle(self):
        print 'got connection from ', self.client_address
        self.wfile.write('connection %s:%s at %s succeed!' % (host, port, ctime()))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print data
            print "RECV from ", self.client_address[0]
            self.request.send(data)


print 'server is running....'
server = SocketServer.ThreadingTCPServer(addr, Servers)
server.serve_forever()
