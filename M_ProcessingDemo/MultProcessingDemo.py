# coding:utf-8


import os
import time
from multiprocessing import Process


def runProcess(name):
    print 'Current Run Process Is %s (%s)' % (name, os.getpid())
    time.sleep(2)
    print time.time()


if __name__ == '__main__':
    print 'Current Process Is %s .' % (os.getpid())
    p1 = Process(target=runProcess, name='P1', args=('P1',))
    p2 = Process(target=runProcess, name='P2', args=('P2',))
    print "New Create Process ......"
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print "Process Is End ///"
