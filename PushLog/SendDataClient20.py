# -*- coding: utf-8 -*-

import socket
import datetime
import time


def sendData(IP, PORT, dataLen, dataContent):
    dt = datetime.datetime.now()
    formatterTime = '%Y-%m-%d-%H-%M-%S%p'
    now = dt.strftime(formatterTime)
    address = (IP, PORT)
    locIP = socket.gethostbyname(socket.gethostname())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)
    buf = 100 * 1024
    try:
        client.sendall(dataLen)
        time.sleep(1)
        client.sendall(dataContent)
        revMsg = client.recv(buf)
        if revMsg == '1':
            client.close()
            print '%s Send To %s : %d Data Success .' % (locIP, IP, PORT)
        else:
            print '%s ReSend To %s : %d Data Failure.' % (locIP, IP, PORT)
            client.close()
            sendData(IP, PORT, dataLen, dataContent)

    except Exception as e:
        print 'sendMsg Occur Exception : %s' % e.message


if __name__ == '__main__':
    ip = '192.168.2.109'
    prot = 10253
    dataContent = 'fghjklgjklfghjh'
    dataLen = str(len(dataContent))
    while True:
        sendData(ip, prot, dataLen, dataContent)
        print '--------------------------------------------------------'
