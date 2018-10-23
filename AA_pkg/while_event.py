# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
while event
------------------------------------------------
"""
import urllib2
import multiprocessing
from multiprocessing.dummy import Pool as threadpool


urls = ['http://www.baidu.com',
        'http://www.baidu.com']

pool = threadpool(4)
results = pool.map(urllib2.urlopen, urls)

pool.close()
pool.join()
for i in results:
    print i
    for j in i:
        print j
        print '-----------------------------------'

