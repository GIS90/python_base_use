#coding:utf-8

import eventlet



def worker(line):
    print 1
    print line
pool = eventlet.GreenPool()
for result in pool.imap(worker, open("test.txt", 'r')):
    print 2
    print(result)