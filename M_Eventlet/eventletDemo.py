#coding:utf-8

import eventlet as el
import time

def run(work):
    assert isinstance(work, basestring)
    print 'Runing : ' + work
    print time.sleep(2)
    print 'End .............' + work



if __name__=='__main__':

    content = ['cg','tw','cb','sc','za','zz','pp','hx']
    pool = el.GreenPool
    while True:
        pool.spawn(run, 'aaa')
        pool.spawn(run, 'asssa')
        pool.spawn(run, 'aaaa')
