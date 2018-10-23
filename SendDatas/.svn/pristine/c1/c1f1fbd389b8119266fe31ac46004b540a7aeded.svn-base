# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

LOGFILE = "DataServer.log"
MAX_LOG_SIZE = 16 * 1024 * 1024
BACKUP_COUNT = 4
FORMAT = "%(message)s"
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
