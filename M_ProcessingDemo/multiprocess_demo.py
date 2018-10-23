# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import multiprocessing
import random
import time
from multiprocessing import Pool

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/23"


def write(q):
    for value in ['A', 'B', 'C', 'D']:
        print "Put %s to Queue!" % value
        q.put(value)
        time.sleep(random.random())


def read(q, lock):
    while True:
        lock.acquire()
        if not q.empty():
            value = q.get(True)
            print "Get %s from Queue" % value
            time.sleep(random.random())
        else:
            break
        lock.release()


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = Pool()
    lock = manager.Lock()
    pw = p.apply_async(write, args=(q,))
    pr = p.apply_async(read, args=(q, lock))
    p.close()
    p.join()
    print
    print "所有数据都写入并且读完"
