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


def tableTransferToJson(conn, popType, sqlDate, sqlJtqy, path):
    assert isinstance(sqlDate, list)
    assert isinstance(sqlJtqy, dict)
    assert isinstance(popType, list)
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
        cursor = conn.cursor()
        for sqld in sqlDate:
            for pop in popType:
                sqld_new =sqld[0:4] + '-' + sqld[4:6] + '-' +sqld[6:]
                # if pop == 'workder':
                #     pop_new = 'worker'
                # else:
                pop_new = pop
                json = os.path.join(path_new, (sqld_new + pop_new + '.js'))
                if os.path.exists(json):
                    os.unlink(json)
                print '------------' + json + '------------'
                fw = codecs.open(json, 'w', 'utf-8')
                fw.write('var peopleNum={')
                # fw.write('"%s":{' % pop_name)
                fw.write('"peopleD":{')
                for sqlh in range(0, 24, 1):
                    fw.write('"%d":[' % sqlh)
                    if qybh == 'xqbh':
                        sql = "select %s,sum(%s) from qd_population_hour where data_day='%s' and data_hour=%d and %s!=''  GROUP BY %s"\
                              % (qysm, pop, sqld, sqlh, qysm, qysm)
                    else:
                        sql = "select %s,sum(%s) from qd_population_hour where data_day='%s' and data_hour=%d and %s!=''  GROUP BY %s"\
                              % (qysm, pop, sqld, sqlh, qysm, qysm)
                    print pop + ' : ' + sql
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    rNums = len(rows)
                    print 'rNums : %s' % rNums
                    n = 1
                    for row in rows:
                        name = row[0]
                        num = row[1]
                        line = '{"name":"%s","value":%s}' % (name, num)
                        # print line
                        fw.write(line)
                        fw.write(',') if n < rNums else 0
                        n += 1
                    fw.write(']')
                    fw.write(',') if sqlh < 23 else 0
                fw.write('}}')
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
    sqlJtqy = {
        'xqbh': 'xqsm',
        'dqbh': 'dqsm',
        'zqbh': 'zqsm'
    }
    path = r'E:\data\qd_data_js\data\population_hour'
    if conn:
        print info
        tableTransferToJson(conn, popType, sqlDate, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
