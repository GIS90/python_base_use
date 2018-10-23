# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

import socket
import time

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016 / 11 / 24"

print "client start"
host = '127.0.0.1'
port = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('hello from client_1')
data = s.recv(1024)
if data:
    print data
time.sleep(2)

s.close()
print "client end"
