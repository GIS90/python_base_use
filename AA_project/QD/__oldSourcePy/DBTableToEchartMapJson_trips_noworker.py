# -*- coding: utf-8 -*-

# 导包
import pyodbc
import datetime
import os
import codecs


# 获取SQLServer连接对象
def getConnDB(connDriver, connServer, connDB, connUID, connPWD):
    # connect函数的参数设置
    # print 'Connection Information Is :'
    # print 'host :', hostName
    # print 'port :', portNum
    # print 'user :', userName
    # print 'pw :', pw
    # print 'db :', dbName
    # print 'charset :' + 'utf-8'
    # try:
    #     conn = MySQLdb.Connect(host=hostName,
    #                            port=portNum,
    #                            user=userName,
    #                            passwd=pw,
    #                            db=dbName,
    #                            charset='utf8')
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


def tableTransferToJson(conn, sqlDate, workday, jsonPath):
    assert isinstance(sqlDate, list)
    assert isinstance(workday, list)
    cursor = conn.cursor()
    for sqld in sqlDate:
        for wt in workday:
            sqld_new = sqld[0:4] + '-' + sqld[4:]
            js = os.path.join(jsonPath, (wt + sqld_new + '.js'))
            if os.path.exists(js):
                os.unlink(js)
            print '------------' + js + '------------'
            fw = codecs.open(js, 'w', 'utf-8')
            fw.write('var tripsData=[')
            fw.write('\n')
            sql = """
            select g1.leftdqsm, g1.arrdqsm,(g1.nums+g2.nums) as totalnum
            FROM
            (
            select leftdqsm,arrdqsm,sum(noworkder) as nums
            from trips_noworker_jtqy
            where data_month='%s' and leftdqsm!=arrdqsm and workday='%s'
            GROUP BY leftdqsm,arrdqsm
            )g1,
            (
            select leftdqsm,arrdqsm,sum(noworkder) as nums
            from trips_noworker_jtqy
            where data_month='%s' and leftdqsm!=arrdqsm and workday='%s'
            GROUP BY leftdqsm,arrdqsm
            )g2
            where g1.arrdqsm=g2.leftdqsm and g2.arrdqsm=g1.leftdqsm
            ORDER by totalnum
            """%(str(sqld).decode('utf-8'), str(wt).decode('utf-8'),str(sqld).decode('utf-8'), str(wt).decode('utf-8'))
            print sql
            cursor.execute(sql)
            rows = cursor.fetchall()
            rNums = len(rows)
            print 'SQL Rows Is : %d' % rNums
            n = 1
            for row in rows:
                if n % 2 == 1:
                    leftname = row[0]
                    arrname = row[1]
                    num = row[2]
                    line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (leftname, arrname, num)
                    fw.write('\t')
                    fw.write(line)
                    fw.write(',') if n < rNums-1 else 0
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
    connDB = 'qd_json'
    connUID = 'sa'
    connPWD = '123456'

    conn, info = getConnDB(connDriver, connServer, connDB, connUID, connPWD)
    sqlDate = ['201509', '201510']
    workday = ['workday', 'weekend']
    jsonPath = r'E:\data\json\trips_noworker\big'
    if not os.path.exists(jsonPath):
        os.makedirs(jsonPath)
    if conn:
        print info
        tableTransferToJson(conn, sqlDate, workday, jsonPath)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s s' % costTime
