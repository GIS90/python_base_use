# -*- coding: utf-8 -*-

# 日志相关的类和操作


import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import inspect


# 之前getBaseDir属于util模块，为了避免Log模块和util模块形成交叉引用，讲getBaseDir单独出来
def getDirectory():
    """获取程序的根目录，主要用于创建日志文件的目录
       由于采用cxFreeze打包后，目录结构会改变，所以要根据是否为'frozen'来判定
    Args:
        None
    Returns:
        True or False
    Raises:
        None.
    """
    if getattr(sys, "frozen", False):
        # If this is running in the context of a frozen (executable) file,
        # we return the path of the main application executable
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        # If we are running in script or debug mode, we need
        # to inspect the currently executing frame. This enable us to always
        # derive the directory of main.py no matter from where this function
        # is being called
        currentFolder = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(os.path.join(currentFolder, ".."))


CURRENT_FOLDER = os.path.dirname(__file__)
PARENT_FOLDER = os.path.abspath(os.path.join(CURRENT_FOLDER, os.path.pardir))

LOG_FOLDER = os.path.join(getDirectory(), "logs")
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
