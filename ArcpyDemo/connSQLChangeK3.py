# -*- coding:utf-8 -*-

# 导包
import datetime
import pyodbc
import random

import execeptionLogging


# 获取SQLServer连接对象
def connSQL():
    # connect函数的参数设置
    connDriver = '{SQL Server}'
    connServer = 'localhost'
    connDB = 'sde'
    connUID = 'sa'
    connPWD = '123456'

    print 'Test Connect To SQLServer ..........'
    # 用try处理异常
    try:
        # connect连接关键字
        conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                               % (connDriver, connServer, connDB, connUID, connPWD)))

        if conn != -1:
            print 'Connect To SQL Success !'
            return conn
        else:
            print 'Connect To SQL Failure !'
    # 处理异常，自定义异常文件
    except Exception as e:
        print '-----Occur Exception Info :-----'
        logType = 'error'
        logInfo = e.message
        execeptionLogging.log(logType, logInfo)


# 获取conn对象update数据表
def exeUpdateK3Tsql(conn):
    # 获取conn对象的指针
    cursor = conn.cursor()
    tableName = 'sde.DBO.linkRoute'
    print 'Update SQL %s K3............' % tableName
    # update
    sql_select = 'select * from %s' % tableName
    cursor.execute(sql_select)
    tableRows = cursor.fetchall()
    for row in tableRows:
        objectid = row[0]
        try:
            k3 = random.uniform(0, 10)
            sql_update = """
                            update %s
                            set k3=%s
                            where objectid=%s
                       """ % (tableName, k3, objectid)
            cursor.execute(sql_update)
            conn.commit()
            print "%s ----- %s Update Success....... " % (objectid, k3)

        except Exception as e:
            print '-----Occur Exception Info :-----'
            logType = 'error'
            logInfo = e.message
            execeptionLogging.log(logType, logInfo)

    print 'All Rows Update Success !'


if __name__ == '__main__':
    # 获取当前时间
    now = datetime.datetime.now()
    timeFormat = '%Y-%m-%d-%H:%m:%S%p'
    startTime = now.strftime(timeFormat)
    print '********************************************'
    print 'Start Time Is : %s' % startTime

    # 获取SQLServer数据库连接对象conn
    conn = connSQL()
    # 对数据库进行update操作
    exeUpdateK3Tsql(conn)

    # 获取更新后时间，计算脚本运行时间
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
    print '********************************************'
