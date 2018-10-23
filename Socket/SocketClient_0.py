# coding:utf-8


import socket


class socektTcpClient:
    HOST = '192.168.2.127'
    PORT = 5432
    BUFSIZE = 1024 * 1024
    ADDR = (HOST, PORT)

    def __init__(self):
        self.client = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def sendMessToServer(self):
        while True:
            sendData = raw_input('>>>')
            if not sendData:
                break
            self.client.send(sendData.encode('utf-8'))
            recvData = self.client.recv(self.BUFSIZE)
            if not recvData:
                break
            print recvData.encode('utf-8')


if __name__ == '__main__':
    stc = socektTcpClient()
    stc.sendMessToServer()
