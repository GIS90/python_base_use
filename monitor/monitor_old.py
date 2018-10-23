# -*- coding: utf-8 -*-

"""
@author cuiheng
@version 1

"""

import os
import subprocess
import sys
import time
from argparse import ArgumentParser
from datetime import datetime
import stat
import logging
import logging.handlers
import inspect
import socket

lastFileSize = 0
lastModifyTime = None


def getBaseDir():
    retval = ""
    if getattr(sys, "frozen", False):
        # If this is running in the context of a frozen (executable) file,
        # we return the path of the main application executable
        retval = os.path.dirname(os.path.abspath(sys.executable))
    else:
        # If we are running in script or debug mode, we need
        # to inspect the currently executing frame. This enable us to always
        # derive the directory of main.py no matter from where this function
        # is being called
        thisDirectory = os.path.dirname(inspect.getfile(inspect.currentframe()))
        retval = os.path.abspath(os.path.join(thisDirectory, os.pardir))
    return retval


def runCommand(cmd, stdoutToPIPE=True, stderrToPIPE=True):
    assert isinstance(stdoutToPIPE, bool)
    assert isinstance(stderrToPIPE, bool)
    p = None
    if not cmd or not len(cmd):
        warnMsg = "runCommand the command is invalid [%s]" % str(cmd)
        Log.warn(warnMsg)
        return "", ""
    debugMsg = "runCommand the command is [cmd %s] [cwd %s]" % (cmd, os.getcwd())
    Log.info(debugMsg)
    try:
        if stdoutToPIPE and stderrToPIPE:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        elif stdoutToPIPE and not stderrToPIPE:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
        elif not stdoutToPIPE and stderrToPIPE:
            p = subprocess.Popen(cmd, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        elif not stdoutToPIPE and not stderrToPIPE:
            p = subprocess.Popen(cmd, universal_newlines=True, shell=True)
    except Exception, e:
        warnMsg = "runCommand got exception while call subprocess.Popen, error is %s" % str(e)
        Log.warn(warnMsg)
        raise Exception(e)
    else:
        stdoutData, stderrData = p.communicate()
        debugMsg = "runCommand result is [stdout %s] [stderr %s]" % (stdoutData, stderrData)
        Log.debug(debugMsg)
        return stdoutData, stderrData


def createLogInstance():
    Log = logging.getLogger("monitor")
    Log.setLevel(logging.DEBUG)

    _LOG_FORMAT = logging.Formatter("[%(levelname)s][%(asctime)s] [%(filename)s:%(lineno)d] [func: %(funcName)s] :%(message)s")

    _currentTime = datetime.now().strftime('%Y%m%d-%H%M%S')
    _logFileName = _currentTime + "-" + str(os.getpid()) + ".log"

    _CURRENT_DIR = getBaseDir()
    _CURRENT_DIR = os.path.abspath(_CURRENT_DIR)
    _OUTPUT_DIR = os.path.join(_CURRENT_DIR, 'output')
    if not os.path.exists(_OUTPUT_DIR):
        try:
            os.mkdir(_OUTPUT_DIR)
        except Exception, e:
            warnMsg = "make the log directory failed, reason %s" % str(e)
            Log.warn(warnMsg)
            raise Exception(warnMsg)

    _logFileName = os.path.join(_OUTPUT_DIR, _logFileName)
    _logFileName = os.path.abspath(_logFileName)

    _rotateFileHandler = logging.handlers.RotatingFileHandler(_logFileName,
                                                              maxBytes=1024 * 1024 * 16,
                                                              backupCount=8)

    _rotateFileHandler.setFormatter(_LOG_FORMAT)
    Log.addHandler(_rotateFileHandler)

    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setFormatter(_LOG_FORMAT)
    _rotateFileHandler.setFormatter(_LOG_FORMAT)
    Log.addHandler(streamHandler)

    infoMsg = "The log will be logged to file %s" % _logFileName
    Log.info(infoMsg)
    return Log


Log = createLogInstance()


def checkIfFileHasNewError(logFilePath):
    global lastFileSize, lastModifyTime
    if lastFileSize == 0:
        lastFileSize = os.stat(logFilePath).st_size
        lastModifyTime = os.stat(logFilePath).st_mtime
        return False
    currentFileSize = os.stat(logFilePath).st_size
    if currentFileSize < lastFileSize:
        warnMsg = "checkIfFileHasNewError, something weired, file is becoming smaller [current %d] [last %d]" % (currentFileSize, lastFileSize)
        Log.warn(warnMsg)
        return False
    elif currentFileSize == lastFileSize:
        return False
    else:
        currentModifyTime = os.stat(logFilePath).st_mtime
        if currentModifyTime > lastModifyTime:
            # We only consider the difference is valid when the data size difference is bigger than 256
            if currentFileSize - lastFileSize > 256:
                lastFileSize = currentFileSize
                lastModifyTime = currentModifyTime
                return True
            return False
        else:
            warnMsg = "something unknown, file size changed, but the modify time doesn't change [current file size %d] [last file size %d] [last modify time %d] [current modify time %d]" % (currentFileSize, lastFileSize, lastModifyTime, currentModifyTime)
            Log.warn(warnMsg)
            return False


def resetFileSizeAndModifyTime():
    global lastFileSize, lastModifyTime
    lastFileSize = lastModifyTime = 0


def checkArgument(fcdbExePath, logFilePath):
    fcdbExePath = os.path.abspath(fcdbExePath)
    logFilePath = os.path.abspath(logFilePath)
    if not os.path.exists(fcdbExePath) or not os.path.exists(logFilePath):
        warnMsg = "Either fcdb or logFile doesn't exist [fcdb %s] [logFile %s]" % (fcdbExePath, logFilePath)
        Log.warn(warnMsg)
        raise Exception(warnMsg)
    if not os.access(fcdbExePath, os.R_OK | os.X_OK):
        warnMsg = "Could not executable the fcdb exe"
        Log.warn(warnMsg)
        raise Exception(warnMsg)
    if not os.access(logFilePath, os.R_OK):
        warnMsg = "could not read the log file"
        Log.warn(warnMsg)
        raise Exception(warnMsg)


def checkIsDBAlive(dbIP, dbPort):
    return True


def restartIfHasErrorInFile(restartBashPath,
                            logFilePath,
                            fromDbIP,
                            fromDbPort,
                            writeDbIp,
                            writeDbPort):
    checkArgument(restartBashPath, logFilePath)
    Log.info("checkArgument success, we will start monitor file %s" % logFilePath)
    while True:
        time.sleep(5)
        if checkIfFileHasNewError(logFilePath):
            warnMsg = "We detect the log file has been changed, some error has happened"
            Log.warn(warnMsg)
            if not checkIsDBAlive(fromDbIP, fromDbPort):
                warnMsg = "From DB is not alive"
                Log.warn(warnMsg)
            if not checkIsDBAlive(writeDbIp, writeDbPort):
                warnMsg = "Write DB is not alive"
                Log.warn(warnMsg)
            resetFileSizeAndModifyTime()
            runCommand(restartBashPath)


def getArgs(configPath):
    configPath = os.path.abspath(configPath)
    if not os.path.exists(configPath):
        warnMsg = "The configuration doesn't exist %s" % configPath
        Log.warn(warnMsg)
        raise Exception(warnMsg)
    import ConfigParser
    config = ConfigParser.RawConfigParser()
    config.read(configPath)
    restartBashPath = config.get('config', 'restartBashPath')
    logFilePath = config.get('config', 'logFilePath')
    fromDbIP = config.get('config', 'readDbIp')
    fromDbPort = config.get('config', 'readDbPort')
    writeDbIp = config.get('config', 'writeDbIp')
    writeDbPort = config.get('config', 'writeDbPort')
    return restartBashPath, logFilePath, fromDbIP, fromDbPort, writeDbIp, writeDbPort


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage is python monitor monitor.ini"
        sys.exit(1)
    restartBashPath, logFilePath, fromDbIP, fromDbPort, writeDbIp, writeDbPort = getArgs(sys.argv[1])
    restartIfHasErrorInFile(restartBashPath, logFilePath, fromDbIP, fromDbPort, writeDbIp, writeDbPort)
