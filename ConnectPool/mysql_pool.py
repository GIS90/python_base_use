# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import DBUtils.PooledDB as Pooldb
import MySQLdb

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/19"


class Mysql(object):
    conn = None
    __pool = None

    def __init__(self):
        self.__pool = self.__initpool()
        self.conn = self.__getconn()

    def __initpool(self):
        if Mysql.__pool is None:
            print 'Initial pool'
            try:
                pool = Pooldb(creator=MySQLdb, mincached=1, maxcached=200,

                              maxshared=200, maxconnections=200, blocking=False,
                              maxusage=None, setsession=None, reset=True,
                              failures=None, ping=1)
            except Exception as e:
                print 'Initial pool error: %s' % e.message
                return
            else:
                return pool

        def __getconn(self):
            pass




print 'Gao: When will you be my wife?'
print 'WenJuan: Now'
