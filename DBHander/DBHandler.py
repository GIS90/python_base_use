# -*- coding: utf-8 -*-

# DBHandler基于ORM的方式对数据库进行初步的维护，包括
# 1) 监测数据表的数据
# 2）数据的导入和导出
# 3）数据表的定期维护
# 注意:①暂时不支持SQL server的以windows的账号登录的方式
#      ②初始化类的时候必须要穿8个参数，无参数的可以为''

# try:
#     import sqlalchemy
# except Exception, e:
#     msg = "The sqlalchemy is not properly installed, you should check it first!"
#     raise Exception(msg)


class DBType(object):
    MYSQL = 0
    SQL_SERVER = 1
    ORACLE = 2
    SQL_LITE = 3
    OTHER = 4


class DBHandler:
    def __init__(self):
        import yaml
        yamlFile = r'E:\SVN\PAM\config\dev_192.168.3.21.yaml'
        yamlContent = yaml.load(file(yamlFile))
        self.mDbType = yamlContent['database']['type']
        self.mIP = yamlContent['database']['url']
        self.mUser = yamlContent['database']['user']
        self.mPassword = yamlContent['database']['password']
        self.mPort = yamlContent['database']['port']
        self.mDBDefault = yamlContent['database']['default']

    # 依据dbType的不同对数据库进行不同的connect
    # 连接成功返回connect对象，失败返回-1。，
    def connect(self):
        if self.mDbType == DBType.MYSQL:
            import MySQLdb

            conn = MySQLdb.Connect(host=self.mIP,
                                   port=self.mPort,
                                   user=self.mUser,
                                   passwd=self.mPassword,
                                   db=self.mDBDefault,
                                   charset='utf8')
            if conn:
                return conn
            else:
                return -1

        elif self.mDbType == 'SQLServer':
            import pyodbc
            Driver = '{SQL Server}'
            conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                                   % (Driver, self.mIP, self.mDBDefault, self.mUser, self.mPassword)))
            if conn:
                return conn
            else:
                return -1

        elif self.mDbType == DBType.ORACLE:
            import cx_Oracle

            connParas = self.mUser + '/' + self.mPassword + '@' + self.mIP + '/' + 'orcl'
            conn = cx_Oracle.connect(connParas)
            if conn:
                return conn
            else:
                return -1

        elif self.mDbType == DBType.SQL_LITE:
            import sqlite3
            dbName = self.mDBDefault + '.db'
            conn = sqlite3.connect(dbName)
            if conn:
                return conn
            else:
                return -1

        elif self.mDbType == 4:
            pass
        else:
            pass

    def open(self):
        pass

    def close(self):
        self.connect().close()

    def getRecordCountInTable(self):
        pass

    def exportTableToFile(self, tableName, pathName):
        pass

    def importFromXLS(self, xlsPath):
        pass

    def truncateTable(self, tableData):
        pass

    def appendData(self):
        pass

    def inpTotal05(self):
        print 11
        connDB = DBHandler().connect()
        print connDB


if __name__ == '__main__':
    DBHandler().inpTotal05()
