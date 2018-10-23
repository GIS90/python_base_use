# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/17'
"""


import os
import time

path = r'E:\text\Python\contextlib.txt'

if os.path.exists(path):

    date = time.localtime()
    bakName = os.path.splitext(path)[0]
    for i in range(0, 6):
        if date[i] < 10:
            bakName = bakName + '0' + str(date[i])
        else:
            bakName += str(date[i])
    bakName += os.path.splitext(path)[1]
    os.renames(path, bakName)