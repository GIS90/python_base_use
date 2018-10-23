# -*- coding:utf-8 -*-
"""
    连接SQLServer数据库，更改LinkGeo表ID>4万的K3值
    K3值在1-4范围内
"""
# 导包
import pyodbc
import random
from Log import *
import time


# 获取SQLServer连接对象
def connSQL():
    # connect函数的参数设置
    connDriver = '{SQL Server}'
    connServer = '192.168.88.219'
    connDB = 'sde'
    connUID = 'sde'
    connPWD = 'sde'
    # connDriver = '{SQL Server}'
    # connServer = 'localhost'
    # connDB = 'sde'
    # connUID = 'sa'
    # connPWD = '123456'
    print 'Test Connect To SQLServer ..........'
    # 用try处理异常
    try:
        # connect连接关键字
        SQLConn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                                  % (connDriver, connServer, connDB, connUID, connPWD)))
        if SQLConn:
            print 'Connect To SQL Success !'
            return SQLConn
        else:
            print 'Connect To SQL Failure !'
            return -1
    # 处理异常，自定义异常文件
    except Exception as e:
        print '-----Occur Exception Info : %s' % e.message
        logType = 'error'
        logInfo = e.message
        Log(logType, logInfo)


# 获取conn对象update数据表
def UpdateK3(conn):
    # 获取conn对象的指针
    cursor = conn.cursor()
    tableName = "sde.dbo.LINKTOP"
    print 'Update SQL %s K3..............' % tableName
    sql_select = 'select objectid_1 from %s where id>20000' % tableName
    cursor.execute(sql_select)
    tableRows = cursor.fetchall()
    for row in tableRows:
        objectid_1 = row[0]
        try:
            k3Value = random.uniform(0, 4)
            sql_update = """
                            update %s
                            set k3=%s
                            where objectid_1=%s
                       """ % (tableName, k3Value, objectid_1)
            cursor.execute(sql_update)
            conn.commit()
            print "object_1 = %s ----- k3 = %s Update Success....... " % (objectid_1, k3Value)
        except Exception as e:
            print '-----Occur Exception Info : %s' % e.message
            logType = 'error'
            logInfo = e.message
            Log(logType, logInfo)
    print "All Row Update Success ."
    print '----------------------------------------------------------------'


if __name__ == '__main__':
    exeNum = 1
    rltConn = connSQL()
    while True:
        # 获取当前时间
        now = datetime.datetime.now()
        timeFormat = '%Y-%m-%d-%H:%m:%S%p'
        startTime = now.strftime(timeFormat)
        print 'Current Time Is : %s , Execute Num = %d .' % (startTime, exeNum)
        if rltConn:
            UpdateK3(rltConn)
        time.sleep(60)
        exeNum += 1


