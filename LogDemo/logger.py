# -*- coding: utf-8 -*-

"""
log module record the detailed informations of gps_import_db
"""


import os
import inspect
import logging
from logging.handlers import RotatingFileHandler


CURRENT_DIR = os.path.abspath(os.path.dirname(inspect.stack()[0][1]))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.path.pardir))

LOG_DIR = os.path.abspath(os.path.join(PARENT_DIR, "logs"))
if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
    except Exception as e:
        msg = "make log dir occur: %s." % e.message
        raise msg
LOG_NAME = "logs.log"
LOG_MODE = "a"
LOG_MAX_BYTES = 8 * 1024 * 1024
LOG_BACKUP_COUNT = 5
LOG_LEVEL = logging.DEBUG
LOG_FORMATTER = "%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s"
LOG_FILE = os.path.abspath(os.path.join(LOG_DIR, LOG_NAME))
file_handler = RotatingFileHandler(filename=LOG_FILE,
                                   mode=LOG_MODE,
                                   maxBytes=LOG_MAX_BYTES,
                                   backupCount=LOG_BACKUP_COUNT)
formatter = logging.Formatter(LOG_FORMATTER)
file_handler.setFormatter(formatter)
file_handler.setLevel(LOG_LEVEL)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(LOG_LEVEL)

logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

