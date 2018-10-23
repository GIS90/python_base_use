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


def tableTransferToJson(conn, sqlTime, sqlJtqy, path):
    assert isinstance(sqlTime, list)
    assert isinstance(sqlJtqy, dict)
    for qysm, qymj in sqlJtqy.items():
        if qysm == 'xqsm':
            name = 'smaller'
        elif qysm == 'zqsm':
            name = 'middle'
        elif qysm == 'dqsm':
            name = 'big'
        path_new = os.path.join(path, name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        for sqld in sqlTime:
            sqld_name = sqld[:4] + "-" + sqld[4:]
            js = os.path.abspath(os.path.join(path_new, sqld_name + 'density.js'))
            print '------------%s------------' % js
            fw = codecs.open(js, 'w', 'utf-8')
            fw.write('var outlanderData={')
            fw.write('\r\n')
            fw.write('\t')
            fw.write("'Data':[")
            fw.write("\n")
            cursor = conn.cursor()
            sql = 'select %s,sum(outlander),%s from qd_outlander where data_month = %s and len(%s) > 0 group by %s, %s' % (qysm, qymj, sqld, qysm, qysm, qymj)
            print sql
            cursor.execute(sql)
            rows = cursor.fetchall()
            n = 1
            rNums = len(rows)
            print rNums
            for row in rows:
                name = row[0]
                num = row[1]
                mj = row[2]
                density = int(num / mj * 1000000)
                fw.write('\t')
                line = '{"name":"%s","value":%s}' % (name, density)
                fw.write(line)
                fw.write(',') if n < rNums else fw.write(']')
                n += 1
                fw.write('\r\n')
            fw.write("}")
            fw.close()
            print js, " success...."

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
    path = r'E:\data\qd_data_js\data\outlander\outlander_density'
    sqlTime = ['201509', '201510']
    sqlJtqy = {
        'xqsm': 'xqmj',
        'dqsm': 'dqmj',
        'zqsm': 'zqmj',
    }
    if conn:
        print info
        tableTransferToJson(conn, sqlTime, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
