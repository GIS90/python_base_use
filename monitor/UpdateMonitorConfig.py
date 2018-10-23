# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/6/1'
"""
import os
import datetime


data = []
dirname, basename = os.path.split(__file__)
config = os.path.abspath(os.path.join(dirname, 'monitor.ini'))
f_r = open(config, 'r')
content = f_r.read()
f_r.close()
f_w = open(config, 'w')
cur_ym = datetime.datetime.now().strftime('%Y%m')
up_ym = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y%m')
data.append(content.split(up_ym)[0])
data.append(cur_ym)
data.append(content.split(up_ym)[1])
for d in data:
    f_w.write(d)
f_w.close()
