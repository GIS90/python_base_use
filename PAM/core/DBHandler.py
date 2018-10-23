# -*- coding: utf-8 -*-

# DBHandler基于ORM的方式对数据库进行初步的维护，包括
# 1) 监测数据表的数据
# 2）数据的导入和导出
# 3）数据表的定期维护
# 注意:1)暂时不支持SQL server的以windows的账号登录的方式
#      2)初始化类的时候必须要穿8个参数，无参数的可以为''

# try:
#     import sqlalchemy
# except Exception, e:
#     msg = "The sqlalchemy is not properly installed, you should check it first!"
#     raise Exception(msg)
from Log import Log


class DBType(object):
    MYSQL = 0
    SQL_SERVER = 1
    ORACLE = 2
    SQL_LITE = 3
    OTHER = 4


class DBHandler:
    def __init__(self, dbType, ip, port, user, passWord, default):
        self.mDbType = str(dbType).upper()
        self.mIP = ip
        self.mPort = int(port)
        self.mUser = user
        self.mPassword = passWord
        self.mDBDefault = default
        self.conn = None

    def open(self):
        try:
            return self.__open()
        except Exception as e:
            Log.error("DBHandler open got exception, error is " + str(e))
            return False

            # 依据dbType的不同对数据库进行不同的connect
            # 连接成功返回connect对象，失败返回-1。，
            # def connect(self):

    def __open(self):
        if self.mDbType == 'MYSQL':
            import mysql.connector
            self.conn = mysql.connector.connect(host=self.mIP,
                                        port=self.mPort,
                                        user=self.mUser,
                                        passwd=self.mPassword,
                                        db=self.mDBDefault)
        elif self.mDbType == 'SQLServer':
            import pyodbc
            Driver = '{SQL Server}'
            self.conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                                        % (Driver, self.mIP, self.mDBDefault, self.mUser, self.mPassword)))

        elif self.mDbType == 'ORACLE':
            import cx_Oracle
            connParas = self.mUser + '/' + self.mPassword + '@' + self.mIP + '/' + 'orcl'
            self.conn = cx_Oracle.connect(connParas)

        elif self.mDbType == 'SQL_LITE':
            import sqlite3
            dbName = self.mDBDefault + '.db'
            self.conn = sqlite3.connect(dbName)

        else:
            raise Exception("unsupported DataBase")
        return self.conn

    def close(self):
        try:
            if self.conn is not None:
                self.conn.close()
        except Exception as e:
            Log("DBHandler close got exception, error is Close Failure , " + e.message)

    def query(self, sql, retType, times=5):
        # returnType为1，返回值是1一个值，类型字符串
        # returnType为2，返回值列表
        assert isinstance(sql, basestring)
        assert isinstance(retType, int)
        assert retType in range(1, 3)
        if self.conn is None:
            for i in range(1, times, 1):
                if self.open():
                    break
                if i == times:
                    Log.error('DBHandler query got exception, error is Open Failure')
                    return None

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            retValues = cursor.fetchall()
            if not retValues:
                return "0" if 1 == retType else []
            if retType == 1:
                print '-----------------------' + str(retValues[0][0])
                return str(retValues[0][0])
            elif retType == 2:
                return list(retValues)
        except Exception as e:
            Log.error('DBHandler query got exception, error is query Failure , ' + e.message)
            return None


if __name__ == '__main__':
    dba = DBHandler('MYSQL', '127.0.0.1', 3306, 'root', '123456', 'gps')
    dba.open()
    sq1 = 'select * from test.gps2016bk  limit 100'
    queryRet = dba.query(sq1, 2, 5)
    print queryRet
    sq2 = 'select count(*) from test.gps2016bk '
    queryRet = dba.query(sq2, 1, 5)
    print queryRet
