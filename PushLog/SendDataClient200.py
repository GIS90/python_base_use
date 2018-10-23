# -*- coding: utf-8 -*-

import socket
import datetime


class TCPClient(object):

    def __init__(self, HOST, PORT):
        dt = datetime.datetime.now()
        formatterTime = '%Y-%m-%d-%H-%M-%S%p'
        self.now = dt.strftime(formatterTime)
        self.address = (HOST, PORT)
        self.locIP = socket.gethostbyname(socket.gethostname())
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.address)

    def checkConn(self):
        if self.client:
            print '%s Connect To %s : %d Success .' % (self.locIP, self.address[0], self.address[1])
            return True
        else:
            print '%s Connect To %s : %d Failure , Reconnect Waite For Time.....' % (self.locIP, self.address[0], self.address[1])
            for i in range(1, 5, 1):
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn = self.client.connect(self.address)
                if conn:
                    print '%s Connect To %s : %d Success .' % (self.locIP, self.address[0], self.address[1])
                    break
                if i == 5:
                    print 'Try 5 Connect Occur Exception , Please Inspect Connect .'
                    return False
            return True

    def sendMsg(self, data):
        buf = 100 * 1024
        try:
            self.client.sendall(data)
            revMsg = self.client.recv(buf)
            msg = '1'
            if revMsg == msg:
                self.client.close()
                print '%s Send To %s : %d Data Success .' % (self.locIP, self.address[0], self.address[1])
            else:
                print '%s ReSend To %s : %d Data Failure.' % (self.locIP, self.address[0], self.address[1])
                # self.client.close()
                # client = TCPClient(self.address[0], self.address[1])
                self.sendMsg(data)

        except Exception as e:
            print 'sendMsg Occur Exception : %s' % e.message



