# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:

test to dumpy.map of multiprocess


------------------------------------------------
"""
import multiprocessing
from multiprocessing.dummy import Pool
import time
import threading

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/25"

CPU_COUNT = multiprocessing.cpu_count()


def worker(n):
    print '%s %d start work' % (n, threading.currentThread())
    print time.sleep(2)
    print '%s %d end work' % (n, threading.currentThread())


pool = Pool(processes=CPU_COUNT)

alist = [i for i in range(20)]
print alist
pool.map(worker, alist)
pool.close()
pool.join()

print 'main is end'






