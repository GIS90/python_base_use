# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: t_q1.py
@time: 2016/9/26 10:24
@describe: 
@remark: 
------------------------------------------------
"""


import threading
import random
import time
from Queue import Queue


class Producer(threading.Thread):
    def __init__(self, pname, queue):
        threading.Thread.__init__(self)
        self.data = queue
        self.name = pname

    def run(self):
        for i in range(1, 10, 1):
            data = random.randint(1, 99)
            print "%s %s produce %s to queue" % (time.ctime(), self.getName(), data)
            self.data.put(data)
            time.sleep(1)
        print "%s: %s finished" % (time.ctime(), self.getName())


class Consumer(threading.Thread):
    def __init__(self, cname, queue):
        threading.Thread.__init__(self)
        self.name = cname
        self.data = queue

    def run(self):
        while True:
            try:
                value = self.data.get(1, 5)
                print "--------%s %s consume %s to queue" % (time.ctime(), self.getName(), value)
                time.sleep(2)
            except Exception as e:
                print "%s: %s finished" % (time.ctime(), self.getName())
                break


class Consumer_1(threading.Thread):
    def __init__(self, cname, queue):
        threading.Thread.__init__(self)
        self.name = cname
        self.data = queue

    def run(self):
        while True:
            try:
                value = self.data.get(1, 5)
                print "+++++++%s %s consume %s to queue" % (time.ctime(), self.getName(), value)
                time.sleep(2)
            except Exception as e:
                print "%s: %s finished" % (time.ctime(), self.getName())
                break


if __name__ == "__main__":
    queue = Queue()
    prod = Producer("producer", queue)
    cons = Consumer("consume", queue)
    conss = Consumer("consume_s", queue)
    prod.start()
    cons.start()
    conss.start()
    prod.join()
    conss.join()
    cons.join()





