# coding:utf-8

import threading
import time

Balance = 0
lock = threading.Lock()


def changeBalance(n, m):
    global Balance
    Balance = Balance + n + m
    Balance = Balance - n + m


def runThread(n, m):
    for i in range(1, 1000, 5):
        lock.acquire()
        try:
            changeBalance(n, m)
            print 'Balane = %d; Current Threading Is >>> %s' % (Balance, threading.current_thread().name)
        except Exception as e:
            print e.message
        finally:
            lock.release()


t1 = threading.Thread(target=runThread, name='thread1', args=(5, 10))
t2 = threading.Thread(target=runThread, name='thread2', args=(3, 10))
t1.start()
t2.start()
t1.join()
t2.join()

print Balance
