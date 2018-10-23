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
bufsize = 1024
addr = (host, port)
client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)
data = "7e02000025101004347417001b000000000000030001004f660450c03b010453170118210032010400000000df011ee00103877e"
while True:
    # time.sleep(2)
    print data
    client.sendall(data)
client.close()
