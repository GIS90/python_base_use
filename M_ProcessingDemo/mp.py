# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: mp.py
@time: 2016/10/25 16:58
@describe: 
@remark: 
------------------------------------------------
"""
import multiprocessing
import time


def work(proname, interval):
    print "%s ----- work" % proname
    print multiprocessing.current_process()
    time.sleep(interval)
    print "%s ----- end" % proname


if __name__ == "__main__":

    mp_1 = multiprocessing.Process(target=work, args=("mp_1", 2,))
    mp_2 = multiprocessing.Process(target=work, args=("mp_2", 3,))
    mp_3 = multiprocessing.Process(target=work, args=("mp_3", 2,))
    mp_1.start()
    mp_2.start()
    mp_3.start()
    print multiprocessing.cpu_count()


