# coding=utf-8
import threading
from time import ctime, sleep


def music(func):
    print "I was listening to %s. %s" % (func, ctime())
    sleep(2)
    print 'current threading is :' + str(threading.currentThread().getName())


def move(func):
    print "I was at the %s! %s" % (func, ctime())
    sleep(2)
    print 'current threading is :' + str(threading.currentThread().getName())


threads = []
t1 = threading.Thread(target=music, name='music', args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move, name='movie', args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    print 'current threading is :' + str(threading.currentThread().getName())

    print "all over %s" % ctime()
