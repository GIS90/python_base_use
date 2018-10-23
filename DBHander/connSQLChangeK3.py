# -*- coding:utf-8 -*-

# 导包
import pymssql
import random
import datetime
import time


# 获取SQLServer连接对象
def connSQL():
    # connect函数的参数设置
    connServer = '127.0.0.1'
    connDB = 'CC_sdeDB'
    connUID = 'sa'
    connPWD = '123456'

    print 'Test Connect To SQLServer ..........'
    # 用try处理异常
    try:
        # connect连接关键字
        conn = pymssql.connect(host=connServer, user=connUID, password=connPWD, database=connDB, charset="utf8")

        if conn != -1:
            print conn
            print 'Connect To SQL Success !'
            return conn
        else:
            print 'Connect To SQL Failure !'
    # 处理异常，自定义异常文件
    except Exception as e:
        print '-----Occur Exception Info :-----'
        logInfo = e.message
        print logInfo


# 获取conn对象update数据表
def exeUpdateK3Tsql(conn):
    # 获取conn对象的指针
    cursor = conn.cursor()
    tableName = ['CC_sdeDB.dbo.main']
    for t in tableName:
        print 'Update SQL %s speed............' % t
        # update
        sql_select = 'select * from %s' % t
        cursor.execute(sql_select)
        tableRows = cursor.fetchall()
        if t == 'sde.dbo.main' or t == 'sde.dbo.detail':
            for row in tableRows:
                objectid = row[0]
                try:
                    k3 = random.uniform(0, 50)
                    sql_update = """
                                    update %s
                                    set speed=%s
                                    where objectid=%s
                               """ % (t, k3, objectid)
                    cursor.execute(sql_update)
                    conn.commit()
                    print "%s ----- %s Update Success....... " % (objectid, k3)
                except Exception as e:
                    print '-----Occur Exception Info :-----'
                    print e.message
        else:
            for row in tableRows:
                objectid = row[0]
                try:
                    k3 = random.uniform(0, 20)
                    sql_update = """
                                    update %s
                                    set flowclass=%s
                                    where objectid=%s
                               """ % (t, k3, objectid)

                    cursor.execute(sql_update)
                    conn.commit()
                    print "%s ----- %s Update Success....... " % (objectid, k3)
                except Exception as e:
                    print '-----Occur Exception Info :-----'
                    print e.message

            print '%s All Rows Update Success !' % t


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
    # while True:
    exeUpdateK3Tsql(conn)
    # time.sleep(300)
    # 获取更新后时间，计算脚本运行时间
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
    print '********************************************'
