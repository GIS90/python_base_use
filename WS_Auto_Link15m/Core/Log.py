# -*- coding: utf-8 -*-

# 日志相关的类和操作


import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import inspect


def getcurrdir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        curDir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(os.path.join(curDir, ".."))


CURRENT_FOLDER = os.path.dirname(__file__)
PARENT_FOLDER = os.path.abspath(os.path.join(CURRENT_FOLDER, os.path.pardir))

LOG_FOLDER = os.path.join(getcurrdir(), "Log")
if not os.path.exists(LOG_FOLDER):
    try:
        os.mkdir(LOG_FOLDER)
    except Exception, e:
        msg = "got exception while creating the log folder, error is " + str(e)
        raise Exception(msg)

LOGFILE = os.path.abspath(os.path.join(LOG_FOLDER, "logs.log"))

MAX_LOG_SIZE = 16 * 1024 * 1024
BACKUP_COUNT = 8
FORMAT = "%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s"
LOG_LEVEL = 0

handler = RotatingFileHandler(LOGFILE,
                              mode='a',
                              maxBytes=MAX_LOG_SIZE,
                              backupCount=BACKUP_COUNT)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

Log = logging.getLogger()
Log.setLevel(LOG_LEVEL)
Log.addHandler(handler)

stdoutHandler = logging.StreamHandler(sys.stdout)
stdoutHandler.setFormatter(formatter)
stdoutHandler.setLevel(LOG_LEVEL)
Log.addHandler(stdoutHandler)
