# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: t_lock.py
@time: 2016/9/26 14:47
@describe: 
@remark: 
------------------------------------------------
"""
import threading
import time
import sys



import time,threading

tickts=1000
tickt_code=1000
lock=threading.Lock()

def sales_tick():
	global tickts,tickt_code
	tickts=tickts-1
	tickt_code=tickt_code+1
	print('Your tickt(%s)! (%s)'%(tickt_code,threading.current_thread().name))


def run_thread():
	while True: 		     #循环次数够多导致某个线程被中断，从而导致tickts被改乱
		lock.acquire()		 #因此当某个线程开始执行sales_tick时，给它上一把锁，其它线程不能接近
		global tickts
		if tickts==0:
			lock.release()   #票销售玩
			break
		try:
			sales_tick()
		finally:
			lock.release()

t1=threading.Thread(target=run_thread,name='thread_one')
t2=threading.Thread(target=run_thread,name='thread_two')
t1.start()
t2.start()
t1.join()
t2.join()
print('No tickt')