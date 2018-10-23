# -*- coding: utf-8 -*-

# 导包
import codecs
import datetime
import os
import pyodbc


# 获取SQLServer连接对象
def getConnDB(driver, server, db, user, pwd):
    # 用try处理异常
    try:
        conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                               % (driver, server, db, user, pwd)))
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
        if qysm == 'xqsm':
            dir_name = 'smaller'
        elif qysm == 'zqsm':
            dir_name = 'middle'
        elif qysm == 'dqsm':
            dir_name = 'big'
        path_new = os.path.join(path, dir_name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        cursor = conn.cursor()
        for sqld in sqlDate:
            for pop in popType:
                sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
                json = os.path.join(path_new, (sqld_new + pop + '.js'))
                if os.path.exists(json):
                    os.unlink(json)
                print '------------' + json + '------------'
                fw = codecs.open(json, 'w', 'utf-8')
                fw.write('var peopleNum={')
                fw.write('"peopleD":{')
                for sqlh in range(0, 24, 1):
                    fw.write('"%d":[' % sqlh)
                    if qybh == 'xqbh':
                        sql_main = "select %s,sum(%s),xqmj from qd_population_hour where data_day='%s' and data_hour=%d and %s!=''  GROUP BY %s,xqmj" \
                              % (qysm, pop, sqld, sqlh, qysm, qysm)
                        sql_sub = "select xqsm from cell_distinct"
                        print pop + ' : ' + sql_main
                        cursor.execute(sql_main)
                        rows = cursor.fetchall()
                        rNums = len(rows)
                        print 'rNums : %s' % rNums
                        if rNums > 0:
                            print pop + ' : ' + sql_sub
                            cursor.execute(sql_sub)
                            rows_sub = cursor.fetchall()
                            for row in rows_sub:
                                name = row[0]
                                density = 0
                                line = '{"name":"%s","value":%s}' % (name, density)
                                fw.write(line)
                                fw.write(',')
                        n = 1
                        for row in rows:
                            name = row[0]
                            num = row[1]
                            mj = row[2]
                            density = int(num / mj * 1000000)
                            line = '{"name":"%s","value":%s}' % (name, density)
                            fw.write(line)
                            fw.write(',') if n < rNums else 0
                            n += 1
                        fw.write(']')
                        fw.write(',') if sqlh < 23 else 0
                    elif qybh == 'zqbh':
                        sql = "select %s,sum(%s),zqmj from qd_population_hour where data_day='%s' and data_hour=%d and %s!=''  GROUP BY %s,zqmj" \
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
                            mj = row[2]
                            density = int(num / mj * 1000000)
                            line = '{"name":"%s","value":%s}' % (name, density)
                            fw.write(line)
                            fw.write(',') if n < rNums else 0
                            n += 1
                        fw.write(']')
                        fw.write(',') if sqlh < 23 else 0
                    elif qybh == 'dqbh':
                        sql = "select %s,sum(%s),dqmj from qd_population_hour where data_day='%s' and data_hour=%d and %s!=''  GROUP BY %s,dqmj" \
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
                            mj = row[2]
                            density = int(num / mj * 1000000)
                            line = '{"name":"%s","value":%s}' % (name, density)
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
    time_format = '%Y-%m-%d-%H:%m:%S%p'
    start_time = now.strftime(time_format)
    print 'Start time is : %s' % start_time
    # SQLServer配置
    driver = '{SQL Server}'
    server = 'localhost'
    db = 'qd_db'
    user = 'sa'
    pwd = '123456'
    conn, info = getConnDB(driver, server, db, user, pwd)

    # popType = ['population', 'resident', 'noworker', 'workder',
    #            'outlander', 'passer', 'outlandresident', 'tourist']
    popType = ['population', 'noworker', 'workder', 'outlander']
    sqlDate = ['20150907', '20150908', '20150909', '20150910', '20150911',
               '20150912', '20150913', '20151004', '20151005']
    sqlJtqy = {
        'xqbh': 'xqsm',
        # 'dqbh': 'dqsm',
        # 'zqbh': 'zqsm'
    }
    path = r'E:\data\qd_data_js\data\population_density\population_hour'
    if conn:
        print info
        tableTransferToJson(conn, popType, sqlDate, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds

    print 'PyScript Cost Time Is : %s' % costTime
