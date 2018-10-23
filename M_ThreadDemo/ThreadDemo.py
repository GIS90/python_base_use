#coding:utf-8

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import timer


def loop():
    print 'Current Threading Is : '+threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        timer.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


print '1...Current Threading Is : '+threading.current_thread().name
t=threading.Thread(target=loop,name='LoopThread')
t.start()
print '2...Current Threading Is : '+threading.current_thread().name

