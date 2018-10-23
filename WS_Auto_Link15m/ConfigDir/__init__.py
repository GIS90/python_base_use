# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/30'
"""
from time import strftime, localtime


year = strftime("%Y", localtime())
mon = strftime("%m", localtime())
up_mon = int(mon) - 1
if up_mon < 10:
    up_mon = "0" + str(up_mon)
day = strftime("%d", localtime())
query_time_strat = str(year) + "-" + str(up_mon) + "-" + str(day) + " 00:00:00"
query_time_end = str(year) + "-" + str(mon) + "-" + str(day) + " 00:00:00"

print query_time_end
print query_time_strat