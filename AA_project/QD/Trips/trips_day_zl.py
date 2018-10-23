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
        for sqld in sqlDate:
            sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
            js = os.path.join(path_new, (sqld_new + '.js'))
            if os.path.exists(js):
                os.unlink(js)
            print '------------' + js + '------------'
            fw = codecs.open(js, 'w', 'utf-8')
            fw.write('var tripsData=[')
            fw.write('\n')
            if qysm == "dqsm":
                sql = """
                select g1.leftdqsm, g1.arrdqsm,(g1.nums+g2.nums) as totalnum
                FROM
                (
                select leftdqsm,arrdqsm,sum(trips) as nums
                from qd_trips_day
                where data_day='%s' and leftdqsm!=arrdqsm
                GROUP BY leftdqsm,arrdqsm
                )g1,
                (
                select leftdqsm,arrdqsm,sum(trips) as nums
                from qd_trips_day
                where data_day='%s' and leftdqsm!=arrdqsm
                GROUP BY leftdqsm,arrdqsm
                )g2
                where g1.arrdqsm=g2.leftdqsm and g2.arrdqsm=g1.leftdqsm
                ORDER by totalnum
                """ % (str(sqld).decode('utf-8'), str(sqld).decode('utf-8'))
            elif qysm == "zqsm":
                sql = """
                select g1.leftzqsm, g1.arrzqsm,(g1.nums+g2.nums) as totalnum
                FROM
                (
                select leftzqsm,arrzqsm,sum(trips) as nums
                from qd_trips_day
                where data_day='%s' and leftzqsm!=arrzqsm
                GROUP BY leftzqsm,arrzqsm
                )g1,
                (
                select leftzqsm,arrzqsm,sum(trips) as nums
                from qd_trips_day
                where data_day='%s' and leftzqsm!=arrzqsm
                GROUP BY leftzqsm,arrzqsm
                )g2
                where g1.arrzqsm=g2.leftzqsm and g2.arrzqsm=g1.leftzqsm
                ORDER by totalnum
                """ % (str(sqld).decode('utf-8'), str(sqld).decode('utf-8'))
            # print sql
            cursor.execute(sql)
            rows = cursor.fetchall()
            rNums = len(rows)
            print 'SQL Rows Is : %d' % rNums
            n = 1
            for row in rows:
                if n % 2 == 1:
                    leftname = row[0]
                    arrname = row[1]
                    num = int(row[2])
                    line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (leftname, arrname, num)
                    fw.write('\t')
                    fw.write(line)
                    fw.write(',') if n < rNums - 1 else 0
                    fw.write('\n')
                    n += 1
                else:
                    n += 1
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
    jsonPath = r'E:\data\qd_data_js\data\Trips\Trips_day\zongliang'
    if conn:
        print info
        tableTransferToJson(conn, sqlDate, jsonPath, sqlJtqy)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s s' % costTime
