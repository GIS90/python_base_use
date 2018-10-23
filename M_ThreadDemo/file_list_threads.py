# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: file_list_threads.py
@time: 2016/9/26 11:38
@describe: 
@remark: 
------------------------------------------------
"""

import datetime
import os
import threading
import time
from Queue import Queue


class Producer(threading.Thread):
    def __init__(self, pname, queue, path):
        threading.Thread.__init__(self)
        self.name = pname
        self.__work = queue
        self.__source = path

    def run(self):
        file_lists = os.listdir(self.__source)
        for fname in file_lists:
            file_file = os.path.abspath(os.path.join(self.__source, fname))
            if os.path.isfile(file_file):
                print "%s: %s is producing %s to the queue!" % (time.ctime(), self.name, file_file)
                self.__work.put(file_file)
        print "%s: %s finished." % (datetime.datetime.now(), self.name)


class Consumer(threading.Thread):
    def __init__(self, cname, queue):
        threading.Thread.__init__(self)
        self.name = cname
        self.__work = queue

    def run(self):
        while True:
            try:
                value = self.__work.get(1, 5)
                self.__work.task_done()
                print "%s is consuming %s in the queue is consumed!" % (self.name, value)
                time.sleep(2)
            except Exception as e:
                print "%s: %s finished!" % (time.ctime(), self.name)
                break

if __name__ == '__main__':
    queue = Queue()
    path = r"E:\data\ws\data"
    prod = Producer("producer", queue, path)
    prod.start()
    prod.join()
    for i in range(1, 5, 1):
        consume_name = "consume_" + str(i)
        cons = Consumer(consume_name, queue)
        cons.start()
