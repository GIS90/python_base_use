# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: record info, debug, error, fatial information
of the ArcSDE database migration to other one write to logs.log,

demo:
from log.py import *

msg = "XXXX"
log.info(msg)
log.debug(msg)
log.error(msg)
log.fatial(msg)

------------------------------------------------
"""

import inspect
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/11/29"

# log config
MAX_SIZE = 10 * 1024 * 1024
BACKUP_COUNT = 8
FORMAT = "%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s"
LOG_LEVEL = 0
LOG_DELAY = 2


# get current log.py folder, solve is or not frozen of the script
def get_cur_folder():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(__file__))
    else:
        cur_folder = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(cur_folder)

cur_folder = get_cur_folder()
log_folder = os.path.abspath(os.path.join(get_cur_folder(), "../log"))
if not os.path.exists(log_folder):
    try:
        os.makedirs(log_folder)
    except Exception as e:
        msg = "create log folder is failure: %s" % e.message
        raise Exception(msg)

log_file = os.path.abspath(os.path.join(log_folder, "logs.log"))

# file log
file_handle = RotatingFileHandler(filename=log_file,
                                  mode='a',
                                  maxBytes=MAX_SIZE,
                                  backupCount=BACKUP_COUNT,
                                  encoding=None,
                                  delay=LOG_DELAY)
formatter = logging.Formatter(FORMAT)
file_handle.setFormatter(formatter)
file_handle.setLevel(LOG_LEVEL)

# print log
strout_handle = logging.StreamHandler(sys.stdout)
strout_handle.setFormatter(formatter)
strout_handle.setLevel(LOG_LEVEL)

# log object
log = logging.getLogger()
log.setLevel(LOG_LEVEL)
log.addHandler(file_handle)
log.addHandler(strout_handle)
