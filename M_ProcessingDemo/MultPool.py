# coding:utf-8


import multiprocessing
import os
import random
import time


def runPool(name):
    print 'Run Task %s (%s) .......' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print 'Current Process Is : %s' % os.getpid()
    p = multiprocessing.Pool(5)
    for i in range(5):
        p.apply_async(runPool, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
