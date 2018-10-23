# -*- coding: utf-8 -*-

# 导包
import pyodbc
import datetime
import os
import codecs


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


def tableTransferToJson(conn, sqlJtqy, path):

    assert isinstance(sqlJtqy, dict)
    for qybh, qysm in sqlJtqy.items():
        if qybh == 'xqbh':
            name = 'smaller'
        elif qybh == 'zqbh':
            name = 'minddle'
        elif qybh == 'dqbh':
            name = 'big'
        path_new = os.path.join(path, name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        js = os.path.abspath(os.path.join(path_new, 'workerRW_rw.js'))
        print '------------%s------------' % js
        fw = codecs.open(js, 'w', 'utf-8')
        fw.write('var workerRW_rw=[')
        fw.write('\r\n')
        cursor = conn.cursor()
        if qysm == 'data_name':
            sql = 'select %s,sum(worker) from workerRW_rw_popdensity  group by %s' % (qysm,qysm)
        else:
            sql = 'select %s,sum(worker) from workerRW_rw_popdensity  group by %s' % (qysm,qysm)
        print sql
        cursor.execute(sql)
        rows = cursor.fetchall()
        n = 1
        rNums = len(rows)
        print 'rNums  = %d' % rNums
        for row in rows:
            name = row[0]
            num = row[1]
            fw.write('\t')
            line = '{"name":"%s","value":%s}' % (name, num)
            fw.write(line)
            fw.write(',') if n < rNums else 0
            n += 1
            fw.write('\r\n')
        fw.write(']')
        fw.close()




if __name__ == '__main__':
    # 获取当前时间
    now = datetime.datetime.now()
    timeFormat = '%Y-%m-%d-%H:%m:%S%p'
    startTime = now.strftime(timeFormat)
    print 'Start Time Is : %s' % startTime
    # SQLServer配置
    connDriver = '{SQL Server}'
    connServer = 'localhost'
    connDB = 'qd_js'
    connUID = 'sa'
    connPWD = '123456'
    conn, info = getConnDB(connDriver, connServer, connDB, connUID, connPWD)
    path = r'E:\data\qd_js\workerRW_rw'
    sqlJtqy = {
        'xqbh': 'xqsm',
        'dqbh': 'dqsm',
        'zqbh': 'zqsm',
    }
    if conn:
        print info
        tableTransferToJson(conn, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
