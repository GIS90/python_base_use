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


def tableTransferToJson(conn, sqlDate, jsonPath, sqlJtqy):
    assert isinstance(sqlDate, list)
    assert isinstance(sqlJtqy, list)

    cursor = conn.cursor()
    # 大区
    dqsms = []
    leftDQSM_sql = "select leftdqsm from qd_trips_day where LEN(leftDQSM) > 0  GROUP BY leftdqsm "
    cursor.execute(leftDQSM_sql)
    rows = cursor.fetchall()
    for row in rows:
        for i in row:
            dqsms.append(i)
    arrDQSM_sql = "select arrdqsm from qd_trips_day where LEN(arrDQSM) > 0  GROUP BY arrdqsm "
    cursor.execute(arrDQSM_sql)
    rows = cursor.fetchall()
    for row in rows:
        for i in row:
            if i not in dqsms:
                dqsms.append(i)
    # 中区
    zqsms = []
    leftZQSM_sql = "select leftzqsm from qd_trips_day where LEN(leftZQSM) > 0  GROUP BY leftzqsm "
    cursor.execute(leftZQSM_sql)
    rows = cursor.fetchall()
    for row in rows:
        for i in row:
            zqsms.append(i)
    arrZQSM_sql = "select arrzqsm from qd_trips_day where LEN(arrZQSM) > 0  GROUP BY arrzqsm "
    cursor.execute(arrZQSM_sql)
    rows = cursor.fetchall()
    for row in rows:
        for i in row:
            if i not in zqsms:
                zqsms.append(i)

    for qysm in sqlJtqy:
        if qysm == "xqsm":
            continue
        if qysm == 'xqsm':
            dir_name = 'smaller'
        elif qysm == 'zqsm':
            dir_name = 'minddle'
        elif qysm == 'dqsm':
            dir_name = 'big'
        path_new = os.path.join(jsonPath, dir_name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)

        if qysm == "dqsm":
            for sqld in sqlDate:
                sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
                js = os.path.join(path_new, (sqld_new + '.js'))
                if os.path.exists(js):
                    os.unlink(js)
                print '------------' + js + '------------'
                fw = codecs.open(js, 'w', 'utf-8')
                fw.write('var tripsData_O=[')
                fw.write('\n')
                for i in range(0, len(dqsms), 1):
                    for j in range(i + 1, len(dqsms), 1):
                        sql = "select sum(trips) from qd_trips_day where leftDQSM = '%s' and arrDQSM = '%s' and data_day = '%s'" % (dqsms[i], dqsms[j], sqld)
                        cursor.execute(sql)
                        rlt = cursor.fetchall()
                        line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (dqsms[i], dqsms[j], int(rlt[0][0]))
                        fw.write('\t')
                        fw.write(line)
                        fw.write(',') if i != len(dqsms) - 2 else 0
                        fw.write('\n')
                fw.write(']')
                fw.write('\n')
                fw.write('var tripsData_D=[')
                fw.write('\n')
                for i in range(len(dqsms) - 1, 0, -1):
                    for j in range(i - 1, -1, -1):
                        sql = "select sum(trips) from qd_trips_day where leftDQSM = '%s' and arrDQSM = '%s' and data_day = '%s'" % (dqsms[i], dqsms[j], sqld)
                        cursor.execute(sql)
                        rlt = cursor.fetchall()
                        line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (dqsms[i], dqsms[j], int(rlt[0][0]))
                        fw.write('\t')
                        fw.write(line)
                        fw.write(',') if i != 1 else 0
                        fw.write('\n')
                fw.write(']')
                fw.close()
                print js + 'Generator Success . . . '
        if qysm == "zqsm":
            for sqld in sqlDate:
                sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
                js = os.path.join(path_new, (sqld_new + '.js'))
                if os.path.exists(js):
                    os.unlink(js)
                print '------------' + js + '------------'
                fw = codecs.open(js, 'w', 'utf-8')
                fw.write('var tripsData_O=[')
                fw.write('\n')
                for i in range(0, len(zqsms), 1):
                    for j in range(i + 1, len(zqsms), 1):
                        sql = "select sum(trips) from qd_trips_day where leftZQSM = '%s' and arrZQSM = '%s' and data_day = '%s'" % (zqsms[i], zqsms[j], sqld)
                        cursor.execute(sql)
                        rlt = cursor.fetchall()
                        if not rlt:
                            line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (zqsms[i], zqsms[j], int(rlt[0][0]))
                            fw.write('\t')
                            fw.write(line)
                            fw.write(',') if i != len(zqsms) - 2 else 0
                            fw.write('\n')
                fw.write(']')
                fw.write('\n')
                fw.write('var tripsData_D=[')
                fw.write('\n')
                for i in range(len(zqsms) - 1, 0, -1):
                    for j in range(i - 1, -1, -1):
                        sql = "select sum(trips) from qd_trips_day where leftZQSM = '%s' and arrZQSM = '%s' and data_day = '%s'" % (zqsms[i], zqsms[j], sqld)
                        cursor.execute(sql)
                        rlt = cursor.fetchall()
                        if not rlt:
                            line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (zqsms[i], zqsms[j], int(rlt[0][0]))
                            fw.write('\t')
                            fw.write(line)
                            fw.write(',') if i != 1 else 0
                            fw.write('\n')
                fw.write(']')
                fw.close()
                print js + 'Generator Success . . . '


if __name__ == '__main__':
    # 获取当前时间
    now = datetime.datetime.now()
    timeFormat = '%Y-%m-%d-%H:%m:%S%p'
    startTime = now.strftime(timeFormat)
    print 'Start Time Is : %s' % startTime
    connDriver = '{SQL Server}'
    connServer = 'localhost'
    connDB = 'qd_db'
    connUID = 'sa'
    connPWD = '123456'

    conn, info = getConnDB(connDriver, connServer, connDB, connUID, connPWD)
    sqlDate = ['20150903', '20150904', '20150905', '20150906', '20150907', '20150908',
               '20150909', '20150910', '20150911', '20150912', '20150913', '20150914',
               '20150915', '20150916', '20150917', '20150918', '20151001', '20151002',
               '20151003', '20151004', '20151005', '20151006', '20151007']
    sqlJtqy = ['xqsm', 'dqsm', 'zqsm']
    jsonPath = r'E:\data\qd_data_js\data\Trips\Trips_day\fenfangxiang'
    if conn:
        print info
        tableTransferToJson(conn, sqlDate, jsonPath, sqlJtqy)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s s' % costTime
