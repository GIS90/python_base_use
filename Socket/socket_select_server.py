# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

import select
import socket

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016 / 11 / 24"


print "server start"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 8899))
server.listen(5)
inputs = [server]
while 1:
    rs, ws, es = select.select(inputs, [], [], 1)
    for r in rs:
        if r is server:
            clientsock, clientaddr = r.accept()
            inputs.append(clientsock)
        else:
            data = r.recv(1024)
            if not data:
                inputs.remove(r)
            else:
                print data
print "server end"
