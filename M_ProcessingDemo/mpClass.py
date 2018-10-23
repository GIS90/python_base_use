# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: mpClass.py
@time: 2016/10/26 15:00
@describe: 
@remark: 
------------------------------------------------
"""

import multiprocessing
import time


class WorkProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        for i in range(5):
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)


if __name__ == "__main__":
    wp = WorkProcess(2)
    wp.daemon = True
    wp.start()
    wp.join()

print "end"
