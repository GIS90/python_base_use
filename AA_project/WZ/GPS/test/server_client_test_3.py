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
n = 1
with open('gps.txt') as f:
    for line in f.readlines():
        line = line.split('\n')[0]
        time.sleep(1)
        client.sendall(line)
        print line
        n += 1
        if n % 1000 == 0:
            print n
        print n
client.close()
print 'end'
