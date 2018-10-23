# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
多进程，但是不源于一个父进程直接的多进程之间的

数据共享
------------------------------------------------
"""
# import os
# from multiprocessing import Process, Manager, Lock
#
# lock = Lock()
# manager = Manager()
# sum = manager.Value('tmp', 0)
#
#
# def testFunc(cc, lock):
#     with lock:
#         sum.value += cc


if __name__ == '__main__':
    # threads = []
    #
    # for ll in range(100):
    #     t = Process(target=testFunc, args=(1, lock))
    #     t.daemon = True
    #     threads.append(t)
    #
    # for i in range(len(threads)):
    #     threads[i].start()
    #
    # for j in range(len(threads)):
    #     threads[j].join()
    #
    # print "------------------------"
    # print 'process id:', os.getpid()
    # print sum.value
    for i in range(100000):
        pass