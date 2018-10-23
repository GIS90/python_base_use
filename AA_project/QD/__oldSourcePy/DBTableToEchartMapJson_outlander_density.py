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


def tableTransferToJson(conn, sqlTime, sqlJtqy, path):
    assert isinstance(sqlTime, list)
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
        js = os.path.abspath(os.path.join(path_new, 'outlander.js'))
        print '------------%s------------' % js
        fw = codecs.open(js, 'w', 'utf-8')
        fw.write('var outlanderData={')
        fw.write('\r\n')
        fw.write('\t')
        for sqld in sqlTime:
            if sqld == '201509':
                sqlv = 'Sep'
                fw.write("'%s':[" % sqlv)
            else:
                sqlv = 'Oct'
                fw.write('\t')
                fw.write("'%s':[" % sqlv)
            fw.write('\r\n')
            cursor = conn.cursor()
            if qysm == 'xqsm':
                sql = 'select %s,convert(int,sum(outlander)/mj_gl) from outlander_popdensity where data_month = %s group by %s,mj_gl' % (qysm, sqld, qysm)
            else:
                sql = 'select %s,sum(outlander) from outlander_jtqy group by %s' % (qysm, qysm)
            print sql
            cursor.execute(sql)
            rows = cursor.fetchall()
            n = 1
            rNums = len(rows)
            for row in rows:
                name = row[0]
                num = row[1]
                fw.write('\t')
                line = '{"name":"%s","value":%s}' % (name, num)
                fw.write(line)
                if sqld == '201509':
                    fw.write(',') if n < rNums else fw.write('],')
                else:
                     if n < rNums:
                        fw.write(',')
                     else:
                        fw.write(']')
                        fw.write('\r\n')
                        fw.write('}')
                n += 1
                fw.write('\r\n')

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
    path = r'E:\data\qd_js\outlander_density'
    sqlTime = ['201509', '201510']
    sqlJtqy = {
        'xqbh': 'xqsm',
        # 'dqbh': 'dqsm',
        # 'zqbh': 'zqsm',
    }
    if conn:
        print info
        tableTransferToJson(conn, sqlTime, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
