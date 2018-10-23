# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: smp.py
@time: 2016/10/26 15:39
@describe: 
@remark: 
------------------------------------------------
"""

import multiprocessing
import time

#
# def worker(s, i):
#     s.acquire()
#     print(multiprocessing.current_process().name + "acquire");
#     time.sleep(i)
#     print(multiprocessing.current_process().name + "release\n");
#     s.release()
#
# if __name__ == "__main__":
#     s = multiprocessing.Semaphore(3)
#     for i in range(5):
#         p = multiprocessing.Process(target = worker, args=(s, i*2))
#         p.start()

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print q.get()    # prints "[42, None, 'hello']"
    p.join()