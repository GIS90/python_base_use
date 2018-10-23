# coding:utf-8

import time
from socket import *
from time import localtime

HOST = ""
PORT = 8898  # 设置侦听端口
BUFSIZ = 1024
ADDR = (HOST, PORT)
sock = socket(AF_INET, SOCK_STREAM)

sock.bind(ADDR)
print "server start"
sock.listen(5)
# 设置退出条件
STOP_CHAT = False
while not STOP_CHAT:
    tcpClientSock, addr = sock.accept()
    while True:
        try:
            data = tcpClientSock.recv(BUFSIZ)
            if data:
                print data
        except:
            tcpClientSock.close()
            break

