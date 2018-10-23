# -*- coding: utf-8 -*-

# 导包
import codecs
import datetime
import os
import pyodbc


# 获取SQLServer连接对象
def getConnDB(connDriver, connServer, connDB, connUID, connPWD):
    # connect函数的参数设置
    print 'Connection Information Is :'
    print 'host :', connServer
    print 'port :', 1433
    print 'user :', connUID
    print 'pw :', connPWD
    print 'db :', connDB
    print 'Test Connect To SQLServer ..........'
    # 用try处理异常
    try:
        # connect连接关键字
        conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                               % (connDriver, connServer, connDB, connUID, connPWD)))
        if conn != -1:
            return conn, 'Connect To SQL Success !'
        else:
            return False, 'Connect To SQL Failure !'
    except Exception as e:
        print '-----Occur Exception Info :-----'
        print e.message


def tableTransferToJson(conn, popType, sqlDate, path):
    assert isinstance(sqlDate, list)
    assert isinstance(popType, list)

    if not os.path.exists(path):
        os.makedirs(path)
    cursor = conn.cursor()
    json = os.path.join(path, 'populationDay.js')
    if os.path.exists(json):
        os.unlink(json)
    print '------------' + json + '------------'
    fw = codecs.open(json, 'w', 'utf-8')
    fw.write('var populationDayData={')
    t = 1
    for sqld in sqlDate:
        fw.write("\n\t")
        sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
        fw.write('"%s":{' % sqld_new)
        n = 1
        for pop in popType:
            sql = "select sum(%s) from population_hour where day = '%s'" % (pop, sqld)
            print sql
            cursor.execute(sql)
            rlt = cursor.fetchall()[0][0]
            line = '"%s":"%d"' % (pop, int(rlt))
            fw.write(line)
            fw.write(',') if n < len(popType) else fw.write("}")
            n += 1
        fw.write(',') if t < len(sqlDate) else 0
        t += 1
    fw.write("\n")
    fw.write('}')
    fw.close()
    print "%s Success ..." % json


if __name__ == '__main__':
    # 获取当前时间
    now = datetime.datetime.now()
    timeFormat = '%Y-%m-%d-%H:%m:%S%p'
    startTime = now.strftime(timeFormat)
    print 'Start Time Is : %s' % startTime
    # SQLServer配置
    connDriver = '{SQL Server}'
    connServer = 'localhost'
    connDB = 'qd_db'
    connUID = 'sa'
    connPWD = '123456'
    conn, info = getConnDB(connDriver, connServer, connDB, connUID, connPWD)

    popType = ['population', 'resident', 'noworker', 'workder',
               'outlander', 'passer', 'outlandresident', 'tourist']
    sqlDate = ['20150907', '20150908', '20150909', '20150910', '20150911',
               '20150912', '20150913', '20151004', '20151005']
    path = r'E:\data\qd_data_js\data\population_day'
    if conn:
        print info
        tableTransferToJson(conn, popType, sqlDate, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds

    print 'PyScript Cost Time Is : %s' % costTime
