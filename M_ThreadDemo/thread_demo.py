# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: thread_demo.py
@time: 2016/9/23 11:00
@describe: 
@remark: 
------------------------------------------------
"""

# import threading
#
#
# def thread_fun(num):
#     for i in range(1, num, 5):
#         print "curreent thread name: %s, n: %d" % (threading.currentThread().getName(), i)
#
#
# def main(thread_num):
#     thread_list = list()
#     for i in range(1, thread_num, 1):
#         thread_name = "thread_%s" % i
#         thread = threading.Thread(target=thread_fun,
#                                   name=thread_name,
#                                   args=(100,))
#         thread_list.append(thread)
#     for th in thread_list:
#         th.start()
#     for th in thread_list:
#         th.join()
#
#
# if __name__ == '__main__':
#     main(4)


import threading


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print self.name

if __name__ == "__main__":
    for thread in range(0, 5):
        t = MyThread()
        t.start()


