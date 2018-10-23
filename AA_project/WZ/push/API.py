# -*- coding: utf-8 -*-

"""
"""
import Queue
import datetime
import os
import random
import sys
import thread
import time
from SocketServer import ThreadingTCPServer, BaseRequestHandler
from threading import *

from log import Log

LISTEN_PORT = 36000

CAR_TIME_DICT = {}

TEST_FLAG = False


class BufferCache(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.mQueue = Queue.Queue()
        self.mRunFlag = False
        self.mConnList = []
        self.mCount = 0
        self.mLastTime = None

    def fakeRun(self):
        Log.info("BufferCache Thread running!")
        while True:
            mb = self.mQueue.get()
            self.sendToListener(mb)
            self.mQueue.task_done()

    def run(self):
        Log.info("BufferCache Thread running!")
        GUESS_NUMBER = random.randint(10, 25)
        while True:
            mb = self.mQueue.get()
            if self.mQueue.qsize() < 400:
                self.mCount += 1
                if not self.mCount % GUESS_NUMBER:
                    sleepValue = random.randint(10, 25)
                    sleepValue /= 10.0
                    time.sleep(sleepValue)
                    self.mCount = 0
                    GUESS_NUMBER = random.randint(10, 25)
            else:
                self.mCount = 0
            buf = self.escapeEachLine(mb)
            if buf:
                Log.info(buf)
                self.sendToListener(buf)
            self.mQueue.task_done()

    def sendToListener(self, data):
        for conn in self.mConnList:
            try:
                conn.sendall(data)
            except Exception, e:
                conn.close()
                self.mConnList.remove(conn)

    def stop(self):
        pass

    def cacheBuffer(self, mb):
        if self.mQueue.qsize() < 1024 * 1024 * 128:
            if mb:
                self.mQueue.put(mb)
        else:
            self.mQueue.queue.clear()
            self.mQueue.put(mb)

    @staticmethod
    def getRandomTimeBefore(timeStart, beforeMin, beforeMax):
        r = random.randint(beforeMin, beforeMax)
        return timeStart - datetime.timedelta(seconds=r)

    @staticmethod
    def escapeEachLine(line):
        global CAR_TIME_DICT
        line = line.strip()
        if line.count(',') != 7:
            return ""
        try:
            lines = line.split(",")
            carID = lines[0]
            lon = lines[2]
            lat = lines[3]
            speed = lines[4]
            angel = lines[5]
            state = lines[6]
            delay = 1
            rTime = None
            now = datetime.datetime.now()
            if carID not in CAR_TIME_DICT:
                rTime = BufferCache.getRandomTimeBefore(now, 1, 6)
            else:
                lastTime = CAR_TIME_DICT[carID]
                timePassed = abs((now - lastTime).seconds)
                if 1 == timePassed or timePassed <= 0:
                    rTime = now
                    delay = random.randint(0, 1)
                elif timePassed > 10:
                    r = random.randint(1, 4)
                    rTime = now - datetime.timedelta(seconds=r)
                    delay = r + random.randint(0, 1)
                else:
                    rTime = now - datetime.timedelta(seconds=random.randint(0, 1))
                    delay = random.randint(0, 1)
            CAR_TIME_DICT[carID] = rTime
            retval = "%s,%s,%s,%s,%s,%s,%s,%s\n" % (carID, rTime.strftime("%Y-%m-%d %H:%M:%S"), lon, lat, speed, angel, state, delay)
            return retval
        except Exception, e:
            Log.warn("got exception during escaping, error is %s" % str(e))
            import traceback

            traceback.print_exc()
            return ""

    @staticmethod
    def escapeBuffer(stringBuffer):
        retList = []
        allLines = stringBuffer.splitlines()
        for eachLine in allLines:
            l = BufferCache.escapeEachLine(eachLine)
            retList.append(l)
        return "\n".join(retList)

    def addListener(self, peerConn):
        if peerConn in self.mConnList:
            return
        self.mConnList.append(peerConn)


bufferCache = None


class TCPServerForBaidu(BaseRequestHandler):
    def setup(self):
        BaseRequestHandler.setup(self)

    def handle(self):
        while True:
            # data = self.request.recv(16 * 1024)
            peerAddr = self.request.getpeername()
            Log.info("got connection request from peer %s, current thread id is %s" % (str(peerAddr), str(currentThread().ident)))
            bufferCache.addListener(self.request)
            data = self.request.recv(16 * 1024)
            if not data:
                break

    def finish(self):
        pass


class MyReceiveHandler(BaseRequestHandler):
    def setup(self):
        BaseRequestHandler.setup(self)

    def handle(self):
        cnt = 0
        peerAddr = ""
        while True:
            data = self.request.recv(32 * 1024)
            peerAddr, peerPort = self.request.getpeername()
            if not data:
                infoMsg = "MyReceiveHandler peer data is empty, we will break the connection"
                Log.info(infoMsg)
                break
            if len(data) > 0:
                Log.debug("we have received buffer with length %d" % len(data))
                cnt += len(data)
                bufferCache.cacheBuffer(data)
                allLines = data.splitlines()
                for eachLine in allLines:
                    bufferCache.cacheBuffer(eachLine)
            else:
                infoMsg = "peer buffer data is empty"
                Log.info(infoMsg)
        try:
            self.request.close()
        except Exception, e:
            print "got exception while shutdown the connection"
        debugMsg = "peer %s shutdown, we will close the connection" % peerAddr
        print debugMsg

    def finish(self):
        print "MyReceiveHandler finish called"


def daemon():
    try:
        pid = os.fork()
        if pid > 0:
            # exit first parent
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1)

    # decouple from parent environment
    os.setsid()
    os.umask(0)

    # do second fork
    try:
        pid = os.fork()
        if pid > 0:
            # exit from second parent
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1)


def createRecv():
    HOST = ""
    PORT_FOR_RECV_BUFFER = 34000
    serverForRecv = ThreadingTCPServer((HOST, PORT_FOR_RECV_BUFFER), MyReceiveHandler)
    serverForRecv.allow_reuse_address = True
    serverForRecv.serve_forever()


def main():
    global bufferCache
    daemon()
    bufferCache = BufferCache()
    bufferCache.start()
    thread.start_new(createRecv, ())
    Log.info("main called")
    HOST = ""
    PORT_FOR_BAIDU = 36000
    serverForBaidu = ThreadingTCPServer((HOST, PORT_FOR_BAIDU), TCPServerForBaidu)
    serverForBaidu.allow_reuse_address = True
    serverForBaidu.serve_forever()


def test():
    # withopen("/Users/mac/Desktop/GPSCode/monitor/Log/output.log", "rw") as out:
    out = open("/Users/mac/Desktop/GPSCode/monitor/Log/output.log", "w+a")
    with open("/Users/mac/Desktop/GPSCode/monitor/Log/monitor.log.110") as f:
        lines = f.readlines()
        for l in lines:
            l = BufferCache.escapeEachLine(l)
            out.write(l)
    processFile("/Users/mac/Desktop/GPSCode/monitor/Log/output.log")


def getCarIDAndTimeFromLine(l):
    l = l.strip()
    if not l:
        return None, None
    if l.count(',') != 7:
        return None, None
    splitResult = l.split(',')
    carID = splitResult[0]
    carTime = datetime.datetime.strptime(splitResult[1], "%Y-%m-%d %H:%M:%S")
    return carID, carTime


def processFile(fileName):
    result = {}
    with open(fileName) as f:
        lines = f.readlines()
        for el in lines:
            carID, carTime = getCarIDAndTimeFromLine(el)
            if not carID:
                continue
            if carID not in result:
                result[carID] = [carTime]
            else:
                result[carID].append(carTime)
    for i in result:
        print i, result[i]


def analysis(fileName):
    result = {}
    with open(fileName) as f:
        lines = f.readlines()
        for el in lines:
            carID, carTime = getCarIDAndTimeFromLine(el)
            if carID not in result:
                result[carID] = [carTime]
            else:
                result[carID].append(carTime)
    for i in result:
        print i, result[i]


if __name__ == '__main__':
    # analysis("/Users/mac/Desktop/GPSCode/monitor/Log/monitor.log.111")
    main()
