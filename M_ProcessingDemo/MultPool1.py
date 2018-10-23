__author__ = 'Administrator'
#coding:utf-8

import multiprocessing
import os
import timer
import random

def queueRead(q):
    while True:
        value=q.get(True)
        print 'Get Queue Value Is : %s'%value
def queueWrite(q):
    for value in ['C','B','A']:
        print 'Put %s to Queue'%value
        q.put(value)
        timer.sleep(1)

if __name__=='__main__':
    q=multiprocessing.Queue()
    pr=multiprocessing.Process(target=queueRead,args=(q,))
    pw=multiprocessing.Process(target=queueWrite,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pw.terminate()