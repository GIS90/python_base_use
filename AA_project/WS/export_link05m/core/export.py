# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    导出脚本，主要针对FcdT_Link05m数据的导出
    导出字段：linkid，speed，k3

useage:


------------------------------------------------
"""
import MySQLdb
import multiprocessing
import datetime

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/21"


fields = ['linkid', 'speed', 'k3']
startime = "2017-03-20 00:00:00"
endtime = "2017-03-21 00:00:00"


def get_cpu_count():
    return multiprocessing.cpu_count()







if __name__ == '__main__':
    pass




