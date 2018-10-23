# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

import time
from socket import *

host = '192.168.2.189'
port = 1990
bufsize = 1024 * 1024 * 16
addr = (host, port)
client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)
data = "7e02000025101004347417001b000000000000030001004f660450c03b010453170118210032010400000000df011ee00103877e"
for i in range(1, 10000):
    if i % 1000 == 0:
        print i
    client.sendall(data)
time.sleep(2)
client.sendall('asskjgh')
client.close()
print 'end'
