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

def tableTransferToJson(conn, popType, sqlDate, sqlPeriod, sqlJtqy, path):
    assert isinstance(popType, list)
    assert isinstance(sqlDate, list)
    assert isinstance(sqlPeriod, dict)
    assert isinstance(sqlJtqy, dict)

    for (qybh, qysm) in sqlJtqy.items():
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
        for wt in weekType:
            for sqld in sqlDate:
                for (key, value) in sqlPeriod.items():
                    perKey = key
                    perValue = value
                    for pop in popType:
                        sqld_new =sqld[0:4] + '-' + sqld[4:]
                        if pop == 'workder':
                            pop_new = 'worker'
                        else:
                            pop_new = pop
                        js = os.path.join(path_new, (wt + sqld_new + perKey + pop_new + '.js'))
                        if os.path.exists(js):
                            os.unlink(js)
                        print '------------' + js + '------------'
                        fw = codecs.open(js, 'w', 'utf-8')
                        fw.write('var peopleNum=[')
                        if qysm == 'xqsm':
                            # sql = "select %s,%s from population_period_avg_jtqy where data_month='%s' and period='%s' and workday = '%s' GROUP BY %s，%s"\
                            #       % (qysm, pop, sqld, str(perValue).decode('utf-8'), wt, qysm, pop)
                            sql = "select %s,convert(int,sum(%s)/mj_gl) from population_period_avg_popdensity where data_month='%s' and period='%s' and workday = '%s' GROUP BY %s,mj_gl"\
                                  % (qysm, pop, sqld, str(perValue).decode('utf-8'), wt, qysm)
                        else:
                            sql = "select %s,sum(%s) from population_period_avg_jtqy where data_month='%s' and period='%s' and workday = '%s' GROUP BY %s"\
                                  % (qysm, pop, sqld, str(perValue).decode('utf-8'), wt, qysm)
                        print sql
                        try:
                            cursor.execute(sql)
                            rows = cursor.fetchall()
                            rNums = len(rows)
                            print "Nums = %d" % rNums
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
                        except Exception as e:
                            print 'Exception : '
                            print e.message + '^^^^^^^^^^^^^^^^^'


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

    popType = ['population', 'resident', 'noworker', 'workder', 'outlander', 'passer', 'outlandresident', 'tourist']
    sqlDate = ['201509', '201510']
    sqlPeriod = {'yj': '夜间',
                 'cgf': '早高峰',
                 'wj': '晚间',
                 'wgf': '晚高峰',
                 'bt': '白天'}
    weekType = ['workday', 'weekend']
    sqlJtqy = {
        'xqbh': 'xqsm',
        # 'dqbh': 'dqsm',
        # 'zqbh': 'zqsm'
    }
    path = r'E:\data\qd_js\population_period_avg_density'
    if conn:
        print info
        tableTransferToJson(conn, popType, sqlDate, sqlPeriod, sqlJtqy, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
