# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
------------------------------------------------
"""

import time
from socket import *

host = '127.0.0.1'
port = 1990
bufsize = 1024
addr = (host, port)
client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)
data = '{"body":{"cdbh":"12","clsd":"40","fxbh":"1","hphm":"苏E12345","jdz":"112.2465641","jgsj":1481784684971,"kkmc":"太原清远测试卡口","wdz":"37.90242936"},"command":"Taiyuan_Demo","protocolType":"1"}'
while True:
    print data
    client.sendall(data)
    time.sleep(5)
client.close()
