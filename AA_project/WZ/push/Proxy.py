# -*- coding: utf-8 -*-

"""
"""
from threading import *
import socket
from Queue import Queue
from log import Log
import time


CACHE_SIZE = 16 * 1024
HOST = ""
PORT = 33250
DEBUG = True


class Sender(Thread):
    def __init__(self, dstIP="117.78.3.71", dstPort=36000):
        Thread.__init__(self)
        self.mDstIP = dstIP
        self.mDstPort = dstPort
        self.mQueue = Queue()
        self.mSocket = None

    def sendTCPData(self, mb):
        self.mQueue.put(mb)

    def run(self):
        self.reConnect()
        while True:
            mb = self.mQueue.get()
            self.realSendBuffer(mb)
            self.mQueue.task_done()

    def realSendBuffer(self, mb):
        if not self.mSocket:
            self.reConnect()
        try:
            self.mSocket.sendall(mb)
        except Exception, e:
            self.mSocket.close()
            self.reConnect()

    def reConnect(self):
        Log.info("reConnect called")
        if self.mSocket:
            try:
                self.mSocket.close()
            except Exception, e:
                infoMsg = "got exception while close the socket, error is %s" % str(e)
                Log.info(infoMsg)
        while True:
            try:
                ADDRESS = (self.mDstIP, self.mDstPort)
                self.mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.mSocket.settimeout(10)
                self.mSocket.connect(ADDRESS)
            except Exception, e:
                errMsg = "reConnect failed, error is %s %s" % (str(e), self.mDstIP)
                Log.error(errMsg)
                self.mSocket = None
                if self.mQueue.qsize() > 1024 * 1024:
                    self.mQueue.queue.clear()
                time.sleep(1)
            else:
                self.mSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 16 * 1024 * 1024)
                self.mSocket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 16 * 1024 * 1024)
                break
        infoMsg = "socket create success"
        Log.info(infoMsg)


class Proxy(Thread):
    def __init__(self, recvIP="10.212.142.34", dstIP="117.78.3.71", dstPort=36000):
        Thread.__init__(self)
        self.mRecvIP = recvIP
        self.mDstIP = dstIP
        self.mDstPort = dstPort
        self.mRecvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mRecvSocket.bind((HOST, PORT))
        self.mRecvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 16 * 1024 * 1024)
        self.mTCPSender = Sender()
        self.mTCPSender.start()

    def run(self):
        recvLen = 0
        while True:
            message, (peerAddress, peerPort) = self.mRecvSocket.recvfrom(64 * 1024)
            if peerAddress != self.mRecvIP:
                infoMsg = "IP address doesn't match peer %s local %s" % (peerAddress, self.mRecvIP)
                Log.info(infoMsg)
                continue
            self.mTCPSender.sendTCPData(message)
            if DEBUG:
                recvLen += len(message)
                Log.info("we have received total length is %f KB" % (recvLen / 1024.0))


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 0:
        DEBUG = False
    else:
        if len(sys.argv) > 1 and sys.argv[1].lower() == "-d":
            DEBUG = True
    msg = "DEBUG mode is set to %s" % str(DEBUG)
    print msg
    try:
        p = Proxy()
        p.start()
    except Exception, e:
        warnMsg = "got exception while the program is running, error is %s" % str(e)
        print warnMsg
        import traceback
        traceback.print_stack()
