# -*- coding: utf-8 -*-
import ConfigParser
import argparse
import datetime
import inspect
import os
import socket
import sys
import time
from Queue import Queue
from collections import namedtuple
from threading import *

from log import Log

GPSInfo = namedtuple("GPSInfo", "gpsTime plateNumber lon lat angle gpsSpeed linkID linkSpeed linkPos")
SLEEP_INTERVAL = 100
CACHE_SIZE = 16 * 1024

DEBUG = False
SEND_LENGTH = 0


def getBaseDir():
    RETVAL = ""
    if getattr(sys, "frozen", False):
        # If this is running in the context of a frozen (executable) file,
        # we return the path of the main application executable
        RETVAL = os.path.dirname(os.path.abspath(sys.executable))
    else:
        # If we are running in script or debug mode, we need
        # to inspect the currently executing frame. This enable us to always
        # derive the directory of main.py no matter from where this function
        # is being called
        RETVAL = os.path.dirname(inspect.getfile(inspect.currentframe()))
    infoMsg = "current folder is %s" % RETVAL
    Log.info(infoMsg)
    return RETVAL


class BufferSender(Thread):
    def __init__(self, dst_ip, dst_port):
        Thread.__init__(self)
        self.dstIP = str(dst_ip.strip())
        self.dstPort = int(dst_port)
        self.queue = Queue()
        self.mBufferCache = ""
        self.mLastSendTime = None
        self.mSendCount = 0
        self.mRunFlag = False

    def sendGPSInfo(self, buf):
        self.queue.put(buf)

    @staticmethod
    def getBufferForGPS(gpsInfo):
        gpsTime = gpsInfo.gpsTime
        plateNumber = gpsInfo.plateNumber
        lon = gpsInfo.lon
        lat = gpsInfo.lat
        angle = gpsInfo.angle
        gpsSpeed = gpsInfo.gpsSpeed
        linkID = gpsInfo.linkID
        linkSpeed = gpsInfo.linkSpeed
        linkPos = gpsInfo.linkPos
        return ",".join([gpsTime, plateNumber, lon, lat, angle, gpsSpeed, linkID, linkSpeed, linkPos])

    def sendLeftBuffer(self):
        pass

    def startRun(self):
        self.mRunFlag = True
        self.start()

    def stopRun(self):
        self.mRunFlag = False

    def sendAllBufferInCache(self, sock):
        sock.sendto(self.mBufferCache, (self.dstIP, self.dstPort))
        self.mBufferCache = ""

    @staticmethod
    def checkIfDataValid(buf):
        line = buf.strip()
        valueList = line.split(",")
        if len(valueList) != 9:
            return False
        plateNumber = valueList[1] if not valueList[1].endswith("\N") else ""
        return plateNumber != ""

    def realSendBuffer(self, sock, buf):
        # buf = BufferSender.getBufferForGPS(gpsInfo)
        if DEBUG:
            global SEND_LENGTH
            SEND_LENGTH += len(buf)
            infoMsg = "total send length is %f KB" % (SEND_LENGTH / 1024.0)
            Log.info(infoMsg)
        if len(buf) > 0:
            if self.checkIfDataValid(buf):
                self.mSendCount += 1
                self.mBufferCache += buf
            else:
                Log.warn("realSendBuffer the data is not valid " + str(buf))
        if None == self.mLastSendTime:
            self.mLastSendTime = datetime.datetime.now()
        if len(self.mBufferCache) >= 20 * 1024:
            self.sendAllBufferInCache(sock)
            if None == self.mLastSendTime:
                self.mLastSendTime = datetime.datetime.now()
                return
            else:
                currentTime = datetime.datetime.now()
                delta = currentTime - self.mLastSendTime
                self.mLastSendTime = currentTime
                # we try to smooth the brand width
                time2sleep = SLEEP_INTERVAL - delta.microseconds
                if time2sleep > 0:
                    time.sleep(time2sleep / 1000.0)
        else:
            # if the cache doesn't reach maximum, but timeout, then we still send out all remaining buffer
            currentTime = datetime.datetime.now()
            delta = currentTime - self.mLastSendTime
            if delta.microseconds > 1000:
                self.sendAllBufferInCache(sock)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 16 * 1024 * 1024)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 16 * 1024 * 1024)
        while self.mRunFlag:
            mb = self.queue.get()
            self.realSendBuffer(sock, mb)
            self.queue.task_done()


sender = None


def readConfig(configFile="config.ini"):
    configFile = os.path.join(getBaseDir(), configFile)
    configFile = os.path.abspath(configFile)
    if not os.path.exists(configFile):
        debugMsg = "readConfig got error, the file doesn't exist %s" % configFile
        Log.debug(debugMsg)
        raise Exception(debugMsg)
    if not os.access(configFile, os.R_OK):
        warnMsg = "readConfig the configFile is not readable %s" % configFile
        Log.warn(warnMsg)
        raise Exception(warnMsg)
    configFile = os.path.abspath(configFile)
    cfg = ConfigParser.ConfigParser()
    cfg.read(configFile)
    dirPath = cfg.get("config", "dir")
    filePath = cfg.get("config", "file")
    dstIP = cfg.get("config", "dst_ip")
    dstPort = cfg.get("config", "dst_port")
    debug = cfg.get("config", "debug")
    if debug.lower() == "true":
        global DEBUG
        DEBUG = True
    return dirPath, filePath, dstIP, dstPort


def getTodayStringValue():
    today = datetime.datetime.today()
    return today.strftime("%Y%m%d")


def preProcessForDir(line):
    pass


def preProcessForFile(line):
    line = line.strip()
    valueList = line.split(",")
    if len(valueList) != 9:
        return None
    gpsTime = valueList[0] if not valueList[0].endswith("\N") else ""
    plateNumber = valueList[1] if not valueList[1].endswith("\N") else ""
    lon = valueList[2].rstrip("0") if not valueList[2].endswith("\N") else ""
    lat = valueList[3].rstrip("0") if not valueList[3].endswith("\N") else ""
    angle = valueList[4].rstrip("0") if not valueList[4].endswith("\N") else ""
    gpsSpeed = valueList[5].rstrip("0") if not valueList[5].endswith("\N") else ""
    linkID = valueList[6].rstrip("0") if not valueList[6].endswith("\N") else ""
    linkSpeed = valueList[7].rstrip("0") if not valueList[7].endswith("\N") else ""
    linkPos = valueList[8].rstrip("0") if not valueList[8].endswith("\N") else ""
    return GPSInfo(gpsTime, plateNumber, lon, lat, angle, gpsSpeed, linkID, linkSpeed, linkPos)


def ProcessForFile(filePath):
    with open(filePath) as f:
        allLines = f.readlines()
        for eachLine in allLines:
            # gpsInfo = preProcessForFile(eachLine)
            # if gpsInfo:
            sender.sendGPSInfo(eachLine)
        allLines = None


def monitorDir(dir_path, dst_ip, dst_port):
    pass


def monitorFile(logFileFolder):
    debugMsg = "monitorFile start run, file is %s" % logFileFolder
    Log.info(debugMsg)
    if not os.path.exists(logFileFolder):
        warnMsg = "monitorFile folder doesn't exist %s" % logFileFolder
        raise Exception(warnMsg)
    if not os.path.isdir(logFileFolder):
        warnMsg = "monitorFile folder is not directory %s" % logFileFolder
        raise Exception(warnMsg)
    currentDay = None
    newestDay = None
    batchSet = set()
    while True:
        if not currentDay:
            currentDay = getTodayStringValue()
        if not newestDay:
            newestDay = getTodayStringValue()
        newestDay = getTodayStringValue()
        # Another day starts
        if newestDay != currentDay:
            currentDay = newestDay
            global SEND_LENGTH
            infoMsg = "It's a new day , in the past day, we have all send about %d packet, length %f" % (sender.mSendCount, SEND_LENGTH / 1000.0)
            Log.info(infoMsg)
            sender.mSendCount = 0
            batchSet.clear()
        time.sleep(0.02)
        for eachFile in os.listdir(logFileFolder):
            logfile = os.path.join(logFileFolder, eachFile)
            logfile = os.path.abspath(logfile)
            if not os.path.isfile(logfile):
                continue
            if eachFile.startswith(newestDay):
                if eachFile in batchSet:
                    continue
                else:
                    infoMsg = "we detect a new file " + eachFile
                    Log.info(infoMsg)
                    batchSet.add(eachFile)
                    ProcessForFile(logfile)


def main(monitorMode):
    infoMsg = "main called, monitorMode is %s" % str(monitorMode)
    Log.info(infoMsg)
    dirPath, filePath, dstIP, dstPort = readConfig()
    global sender
    sender = BufferSender(dstIP, dstPort)
    sender.startRun()
    if monitorMode.lower() == "file":
        monitorFile(filePath)
    else:
        monitorDir(dirPath)


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


if __name__ == '__main__':
    daemon()
    parser = argparse.ArgumentParser("get the work mode for the data collection")
    parser.add_argument("-m", "--mode", default="file", help="you must specify which to monitor, dir or file?")
    parser.add_argument("-e", "--escape", default=False)
    mode = ""
    try:
        args = parser.parse_args()
        mode = args.mode
        if not mode.lower() in ["file", "dir"]:
            Log.warn("unsupported mode, we only support file or dir")
            sys.exit(-1)
    except Exception, e:
        Log.error("got exception while launching the program, error is %s" % str(e))
        sys.exit(-1)
    else:
        try:
            main(mode)
        except Exception, e:
            errorMsg = "got exception in main, error is [%s]" % e.message
            Log.error(errorMsg)
            if sender:
                sender.stopRun()
            sys.exit(1)
