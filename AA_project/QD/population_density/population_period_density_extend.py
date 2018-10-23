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


def tableTransferToJson(conn, popType, sqlDate, sqlPeriod, sqlJtqy, path):
    assert isinstance(popType, list)
    assert isinstance(sqlDate, list)
    assert isinstance(sqlPeriod, dict)
    assert isinstance(sqlJtqy, dict)

    for (qybh, qysm) in sqlJtqy.items():
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
            sqld_new = sqld
            if sqld == '20151004' or sqld == '20151005':
                sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
            for (key, value) in sqlPeriod.items():
                perKey = key
                perValue = value
                for pop in popType:
                    js = os.path.join(path_new, (sqld_new + perKey + pop + '.js'))
                    if os.path.exists(js):
                        os.unlink(js)
                    print '------------' + js + '------------'
                    fw = codecs.open(js, 'w', 'utf-8')
                    fw.write('var peopleNum=[')
                    if qysm == 'xqsm':
                        sql = "select %s,sum(%s),xqmj from qd_population_period where data_day='%s' and period='%s' and %s!='' GROUP BY %s, xqmj" \
                              % (qysm, pop, sqld, str(perValue).decode('utf-8'), qysm, qysm)
                        sql_sub = "select xqsm from cell_distinct"
                        print pop + ' : ' + sql_sub
                        cursor.execute(sql_sub)
                        rows_sub = cursor.fetchall()
                        for row in rows_sub:
                            name = row[0]
                            density = 0
                            line = '{"name":"%s","value":%s}' % (name, density)
                            fw.write(line)
                            fw.write(',')
                    elif qysm == 'zqsm':
                        sql = "select %s,sum(%s),zqmj from qd_population_period where data_day='%s' and period='%s' and %s!='' GROUP BY %s, zqmj"\
                              % (qysm, pop, sqld, str(perValue).decode('utf-8'), qysm, qysm)
                    elif qysm == 'dqsm':
                        sql = "select %s,sum(%s),dqmj from qd_population_period where data_day='%s' and period='%s' and %s!='' GROUP BY %s, dqmj"\
                              % (qysm, pop, sqld, str(perValue).decode('utf-8'), qysm, qysm)
                    print sql
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    rNums = len(rows)
                    print 'rNums : %s' % rNums
                    n = 1
                    for row in rows:
                        name = row[0]
                        num = row[1]
                        mj = row[2]
                        density = num / mj * 1000000
                        line = '{"name":"%s","value":%s}' % (name, int(density))
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
    # SQLServer配置
    connDriver = '{SQL Server}'
    connServer = 'localhost'
    connDB = 'qd_db'
    connUID = 'sa'
    connPWD = '123456'
    conn, info = getConnDB(connDriver, connServer, connDB, connUID, connPWD)

    # popType = ['population', 'resident', 'noworker', 'workder', 'outlander', 'passer', 'outlandresident', 'tourist']
    popType = ['population', 'noworker', 'workder', 'outlander']
    sqlDate = ['2015-09-07', '2015-09-08', '2015-09-09', '2015-09-10', '2015-09-11',
               '2015-09-12', '2015-09-13', '20151004', '20151005']
    sqlPeriod = {'yj': '夜间',
                 'cgf': '早高峰',
                 'wj': '晚间',
                 'wgf': '晚高峰',
                 'bt': '白天'}
    sqlJtqy = {
        'xqbh': 'xqsm',
        'dqbh': 'dqsm',
        'zqbh': 'zqsm'
    }
    path = r'E:\data\qd_data_js\data\population_density\population_period'
    if conn:
        print info
        tableTransferToJson(conn, popType, sqlDate, sqlPeriod, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
