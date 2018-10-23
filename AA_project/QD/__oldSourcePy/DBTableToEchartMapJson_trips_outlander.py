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


def tableTransferToJson(conn, sqlDate, sqlPeriod, jsonPath):
    assert isinstance(sqlDate, list)
    assert isinstance(sqlPeriod, dict)
    cursor = conn.cursor()
    for sqld in sqlDate:
        for (key, value) in sqlPeriod.items():
            perKey = key
            perValue = value
            sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
            js = os.path.join(jsonPath, (perKey + sqld_new + 'outlander.js'))
            if os.path.exists(js):
                os.unlink(js)
            print '------------' + js + '------------'
            fw = codecs.open(js, 'w', 'utf-8')
            fw.write('var tripsData=[')
            fw.write('\n')
            # sql = """
            # select g1.leftdqsm, g1.arrdqsm,(g1.nums+g2.nums) as totalnum
            # FROM
            # (
            # select leftdqsm,arrdqsm,sum(outlander) as nums
            # from trips_outlander_jtqy
            # where data_day='%s' and leftdqsm!=arrdqsm and period='%s'
            # GROUP BY leftdqsm,arrdqsm
            # )g1,
            # (
            # select select leftdqsm,arrdqsm,sum(outlander) as nums
            # from trips_outlander_jtqy
            # where data_day='%s' and leftdqsm!=arrdqsm and period='%s'
            # GROUP BY leftdqsm,arrdqsm
            # )g2
            # where g1.arrdqsm=g2.leftdqsm and g2.arrdqsm=g1.leftdqsm
            # ORDER by totalnum,leftdqsm
            # """%(str(sqld).decode('utf-8'), str(perValue).decode('utf-8'),str(sqld).decode('utf-8'), str(perValue).decode('utf-8'))
            sql = """
            select g1.leftzqsm, g1.arrzqsm,(g1.nums+g2.nums) as totalnum
            FROM
            (
            select leftzqsm,arrzqsm,sum(outlander) as nums
            from trips_outlander_jtqy
            where data_day='%s' and leftzqsm!=arrzqsm and period='%s'
            GROUP BY leftzqsm,arrzqsm
            )g1,
            (
            select leftzqsm,arrzqsm,sum(outlander) as nums
            from trips_outlander_jtqy
            where data_day='%s' and leftzqsm!=arrzqsm and period='%s'
            GROUP BY leftzqsm,arrzqsm
            )g2
            where g1.arrzqsm=g2.leftzqsm and g2.arrzqsm=g1.leftzqsm
            ORDER by totalnum,leftdqsm
            """%(str(sqld).decode('utf-8'), str(perValue).decode('utf-8'),str(sqld).decode('utf-8'), str(perValue).decode('utf-8'))
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
    # MySQL配置
    # hostName = '127.0.0.1'
    # portNum = 3306
    # userName = 'root'
    # pw = '123456'
    # dbName = 'jsonmetadb'

    # SQLServer配置
    connDriver = '{SQL Server}'
    connServer = 'localhost'
    connDB = 'qd_json'
    connUID = 'sa'
    connPWD = '123456'

    conn, info = getConnDB(connDriver, connServer, connDB, connUID, connPWD)
    sqlDate = ['20150903', '20150904', '20150905', '20150906', '20150907', '20150908',
               '20150909', '20150910', '20150911', '20150912', '20150913', '20150914',
               '20150915', '20150916', '20150917', '20150918', '20151001', '20151002',
               '20151003', '20151004', '20151005', '20151006', '20151007']
    sqlPeriod = {'yj': ' 夜间',
                 'cgf': ' 早高峰',
                 'wj': ' 晚间',
                 'wgf': ' 晚高峰',
                 'bt': ' 白天'}
    # jsonPath = r'E:\data\json\outlander\big'
    jsonPath = r'E:\data\json\outlander\minddle'
    if not os.path.exists(jsonPath):
        os.makedirs(jsonPath)
    if conn:
        print info
        tableTransferToJson(conn, sqlDate, sqlPeriod, jsonPath)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s s' % costTime
