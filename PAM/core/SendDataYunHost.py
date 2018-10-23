# -*- coding: utf-8 -*-
"""
定义一个SocketClient类进行数据传输，此类为客户端
"""
import socket
from Log import *
import time


class TCPClient(object):
    def __init__(self, HOST, PORT):
        """
        TCPClient初始化，所需参数为Socket连接的IP，PORT
        """
        try:
            self.__address = (HOST, PORT)
            self.__locIP = socket.gethostbyname(socket.gethostname())
            self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__conn = self.__client.connect(self.__address)
        except Exception as initE:
            Log.error('TCPClient init failure : %s' % str(initE.message))

    def checkConn(self, connMax=3):
        """
        检查Socket TCP连接状态,如果初始化连接失败，再次尝试进行连接
        :param connMax: 定义最大连接的次数，默认是3次
        :return: 成功返回True，失败返回False
        """
        if self.__client:
            print '%s Connect To %s : %d Success .' \
                  % (self.__locIP, self.__address[0], self.__address[1])
            return True
        else:
            print '%s Connect To %s : %d Failure , Reconnect Waite For Time.....' \
                  % (self.__locIP, self.__address[0], self.__address[1])
            for i in range(0, connMax, 1):
                try:
                    self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.__conn = self.__client.connect(self.__address)
                    if self.__conn:
                        print '%s Connect To %s : %d Success .' \
                              % (self.__locIP, self.__address[0], self.__address[1])
                        break
                    if i == 5:
                        print 'Try 5 Connect Failure , Please Inspect Connect IP & PORT.'
                        return False
                except Exception as connE:
                    Log.error('TCPClient checkConn Occur Exception : %s' % str(connE.message))
            return True

    def sendMsg(self, data, sendMax=3):
        """
         发送数据包给连接的主机，获取返回结果：
        if mrg=1：
            表示发送数据成功
        else：
            在次发送数据,最大发送次数3次
        :param data: 发送的数据包
        :param sendMax: 定义最大重发送数据次数，默认为3次
        :return: 无
        """
        buf = 100 * 1024
        try:
            self.__client.sendall(data)
            revMsg = self.__client.recv(buf)
            meg = '1'
            if revMsg == meg:
                self.__client.close()
                print '%s Send To %s : %d Data Success .' \
                      % (self.__locIP, self.__address[0], self.__address[1])
            else:
                for i in range(0, sendMax, 1):
                    print '%s Send To %s : %d Data Failure' % \
                          (self.__locIP, self.__address[0], self.__address[1])
                    print 'Waite for Client 5 s , Resend Data.'
                    time.sleep(5)
                    self.sendMsg(data)
                    revMsg = self.__client.recv(buf)
                    if revMsg == meg:
                        self.__client.close()
                        break
        except Exception as sendE:
            Log.error('TCPClient sendMsg Occur Exception : %s' % sendE.message)
