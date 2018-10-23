# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/26'
"""


from Log import *
from AnlyConfigFile import *


class DBHand(object):
    def __init__(self, ):

        self.__TYPE = DB_TYPE
        self.__SERVER = DB_SERVER
        self.__PORT = DB_PORT
        self.__DB = DB_DB
        self.__UID = DB_UID
        self.__PWD = DB_PWD
        self.__conn = None
        self.__cursor = None

    def __open(self):
        if str(self.__TYPE).upper() == 'SQL_SERVER':
            import pyodbc
            DRIVER
            self.conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;PORT=%d;DATABASE=%s;UID=%s;PWD=%s;timeout=30'
                                        % (self.DRIVER, self.__SERVER, self.__PORT, self.__DB, self.__UID, self.__PWD)))

        elif str(self.__TYPE).upper() == 'MYSQL':
            import MySQLdb
            self.conn = MySQLdb.Connect(host=self.__SERVER, port=self.__PORT, user=self.__UID,
                                        passwd=self.__PWD, db=self.__DB, charset='utf8')
        self.cursor = self.conn.cursor()

    def open(self):
        try:
            self.__open()
        except Exception as e:
            Log('ERROR', 'DBHand open Occur Exception : %s' % e.message)

    def close(self):
        try:
            self.conn.close() if self.conn else None
        except Exception as e:
            Log('ERROR', 'DBHand close Occur Exception : %s' % e.message)

    def query(self, sqlType, sql, times=5):
        n = 1
        assert sqlType in range(1, 3)
        assert isinstance(sql, basestring)
        if self.conn is None:
            for i in range(1, times, 1):
                self.open()
                if self.conn:
                    break
                n += 1
            if n == times:
                Log('ERROR', 'DBHandler query got exception, error is Open Failure')
                return None
        try:
            cursor = self.cursor
            cursor.execute(sql)
            retValues = cursor.fetchall()
            if not retValues:
                return "0" if 1 == sqlType else []
            if sqlType == 1:
                return str(retValues[0][0])
            elif sqlType == 2:
                return list(retValues)
        except Exception as e:
            Log('ERROR', 'DBHandler query got exception, error is query Failure , ' + e.message)
            return None
