# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/6/1'
"""

import os
import time
import datetime
import stat

fileStats = os.stat('__init__.py')

print fileStats[stat.ST_SIZE]
timeStamp = fileStats[stat.ST_MTIME]
dateArray = datetime.datetime.fromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print otherStyleTime
print time.ctime(fileStats.st_atime)
print time.ctime(fileStats.st_ctime)
print fileStats.st_ino
print fileStats.st_mtime
print fileStats.st_mode

