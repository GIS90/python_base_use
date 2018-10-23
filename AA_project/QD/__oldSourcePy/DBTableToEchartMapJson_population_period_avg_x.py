# -*- coding: utf-8 -*-

# 导包
import MySQLdb
import datetime
import os
import codecs


# 获取SQLServer连接对象
def getConnDB(hostName, portNum, userName, pw, dbName):
    # connect函数的参数设置
    print 'Connection Information Is :'
    print 'host :', hostName
    print 'port :', portNum
    print 'user :', userName
    print 'pw :', pw
    print 'db :', dbName
    print 'charset :' + 'utf-8'
    try:
        conn = MySQLdb.Connect(host=hostName,
                               port=portNum,
                               user=userName,
                               passwd=pw,
                               db=dbName,
                               charset='utf8')
        if conn != -1:
            return conn, 'Connect To SQL Success !'
        else:
            return False, 'Connect To SQL Failure !'
    except Exception as e:
        print '-----Occur Exception Info :-----'
        print e.message


def tableTransferToJson(conn, popType, sqlDate, sqlPeriod, weekType, jsonPath):
    cursor = conn.cursor()
    for wt in weekType:
        for sqld in sqlDate:
            for (key, value) in sqlPeriod.items():
                perKey = key
                perValue = value
                for pop in popType:
                    sqld_new =sqld[0:4] + '-' + sqld[4:]
                    js = os.path.join(jsonPath, (wt + sqld_new + perKey + pop + '.js'))
                    if os.path.exists(js):
                        os.unlink(js)
                    print '------------' + js + '------------'
                    fw = codecs.open(js, 'w', 'utf-8')
                    fw.write('var peopleNum=[')
                    sql = 'select nameid,%s from population_period_avg_jtxq where data_month="%s" and period="%s" and workday = "%s" GROUP BY population_period_avg_jtxq.nameid'%(pop, sqld, perValue, wt)
                    print sql
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    rNums = len(rows)
                    n = 1
                    for row in rows:
                        name = row[0]
                        num = row[1]
                        line = '{"name":"%s","value":%s}' % (name, num)
                        fw.write(line)
                        fw.write(',') if n < rNums else 0
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
    hostName = '127.0.0.1'
    portNum = 3306
    userName = 'root'
    pw = '123456'
    dbName = 'jsonmetadb'
    conn, info = getConnDB(hostName, portNum, userName, pw, dbName)
    popType = ['population', 'resident', 'noworker', 'worker',
               'outlander', 'passer', 'outlandresident', 'tourist']
    sqlDate = ['201509', '201510']
    sqlPeriod = {'yj': '夜间',
                 'cgf': '早高峰',
                 'wj': '晚间',
                 'wgf': '晚高峰',
                 'bt': '白天'}
    weekType = ['workday', 'weekend']
    sqlJtqy = {
        'xqbh': 'xqsm',
        'dqbh': 'dqsm',
        'zqbh': 'zqsm'
    }
    jsonPath = r'E:\data\qd_js\population_period_avg\xqbh'
    if not os.path.exists(jsonPath):
        os.makedirs(jsonPath)
    if conn:
        print info
        tableTransferToJson(conn, popType, sqlDate, sqlPeriod, weekType, jsonPath)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
