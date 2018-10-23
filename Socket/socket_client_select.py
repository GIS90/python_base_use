# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

import socket

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016 / 11 / 24"

print "client start"
host = '127.0.0.1'
port = 20000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('hello from client')
s.close()
print "client end"
