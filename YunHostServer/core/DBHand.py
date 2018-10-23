# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/26'
数据库ORM
"""


from Log import *


class DBHand(object):
    """
    数据库的初始化，传入相对的参数值
    """
    def __init__(self, DB_type, DB_server, DB_port, DB_db, DB_uid, DB_pwd):
        self.__TYPE = DB_type
        self.__SERVER = DB_server
        self.__PORT = DB_port
        self.__DB = DB_db
        self.__UID = DB_uid
        self.__PWD = DB_pwd
        self.__conn = None
        self.__cursor = None

    def __open(self):
        """
        私有化的open
        :return: 无
        """
        if str(self.__TYPE).upper() == 'SQL_SERVER':
            import pyodbc
            self.__DRIVER = '{SQL Server}'
            self.__conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;PORT=%d;DATABASE=%s;UID=%s;PWD=%s;timeout=30'
                                          % (self.__DRIVER, self.__SERVER, self.__PORT, self.__DB, self.__UID,
                                             self.__PWD)))

        elif str(self.__TYPE).upper() == 'MYSQL':
            import MySQLdb
            self.__conn = MySQLdb.Connect(host=self.__SERVER, port=self.__PORT, user=self.__UID, passwd=self.__PWD,
                                          db=self.__DB, charset='utf8')
        self.__cursor = self.__conn.cursor()

    def open(self):
        """
        外部可调用的数据库open
        :return: 无
        """
        try:
            self.__open()
            return True
        except Exception as openE:
            Log.debug('DBHand open Occur Exception : %s'.decode('utf-8') % openE.message)
            return False

    def close(self):
        """
        关闭数据库
        :return: 无
        """
        try:
            self.__conn.close() if self.__conn else None
        except Exception as closeE:
            Log.debug('DBHand close Occur Exception : %s'.decode('utf-8') % closeE.message)

    def handle(self, sqlData):
        """
        数据库操作流的方法
        :param sqlData: sql语句
        :return: 无
        """
        assert isinstance(sqlData, basestring)
        if self.__conn is None:
            for i in range(1, 5, 1):
                self.open()
                if self.__conn:
                    break
                if i == 5:
                    Log.debug('DBHandler handle occur exception, error is Open Failure')
                    return None
        try:
            cursor = self.__cursor
            cursor.execute(sqlData)
            self.__conn.commit()
            return self.__cursor.rowcount
        except Exception as handleE:
            self.__conn.rollback()
            Log.debug('DBHandler handle occur failure : %s '.decode('utf-8') % handleE.message)
            return 0
        finally:
            self.__cursor.close()
