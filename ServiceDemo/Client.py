# -*- coding: utf-8 -*-

import socket
import datetime


class TCPClient(object):
    host = '192.168.2.129'
    port = 8989
    address = (host, port)
    locIP = socket.gethostbyname(socket.gethostname())
    dt = datetime.datetime.now()
    formatterTime = '%Y-%m-%d-%H-%M-%S%p'
    now = dt.strftime(formatterTime)

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.address)

    def sendMsg(self):
        while True:
            msg = raw_input('%s %s Speak :' % (self.now, self.locIP)).decode('utf-8')
            self.client.sendall(msg)
            if msg.lower() == 'exit':
                break
            data = self.client.recv(10 * 1024)
            if data is None:
                break
            print '%s %s Recall : %s' % (self.now, self.host, data)


if __name__ == '__main__':
    Client = TCPClient()
    Client.sendMsg()

