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


def tableTransferToJson(conn, sqlJtqy, path):
    cursor = conn.cursor()
    for qysm, qymj in sqlJtqy.items():
        if qysm == 'xqsm':
            dir_name = 'smaller'
        elif qysm == 'zqsm':
            dir_name = 'middle'
        elif qysm == 'dqsm':
            dir_name = 'big'
        path_new = os.path.join(path, dir_name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        js = os.path.join(path_new, (qymj + '.js'))
        if os.path.exists(js):
            os.unlink(js)
        print '------------' + js + '------------'
        fw = codecs.open(js, 'w', 'utf-8')
        fw.write('var areaNum=[')
        if qysm == 'xqsm':
            sql = "select xqsm, xqmj from cell_jtxq GROUP BY xqsm, xqmj"
        elif qysm == 'zqsm':
            sql = "select zqsm, zqmj from cell_jtxq GROUP BY zqsm, zqmj"
        elif qysm == 'dqsm':
            sql = "select dqsm, dqmj from cell_jtxq GROUP BY dqsm, dqmj"
        cursor.execute(sql)
        rows = cursor.fetchall()
        rNums = len(rows)
        print 'rNums : %s' % rNums
        n = 1
        for row in rows:
            name = row[0]
            mj = float(row[1]) / 1000000
            line = '{"name":"%s","value":%f}' % (name, mj)
            fw.write("\n")
            fw.write("\t")
            fw.write(line)
            fw.write(',') if n < rNums else 0
            n += 1
        fw.write("\n")
        fw.write(']')
        fw.close()
    print js + 'Success ...'


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

    sqlJtqy = {
        'xqsm': 'xqmj',
        'dqsm': 'dqmj',
        'zqsm': 'zqmj'
    }
    path = r'E:\data\qd_data_js\data\area'
    if conn:
        print info
        tableTransferToJson(conn, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
