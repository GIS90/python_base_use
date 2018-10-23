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

def tableTransferToJson(conn, popType, sqlDate, sqlPeriod, weekType, path):
    cursor = conn.cursor()
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
        for wt in weekType:
            for sqld in sqlDate:
                for pop in popType:
                    nd = sqld[0:4] + '-' + sqld[4:]
                    if pop == 'workder':
                        pop_new = 'worker'
                    else:
                        pop_new = pop
                    js = os.path.join(path_new, (wt + nd + pop_new + '.js'))
                    if os.path.exists(js):
                        os.unlink(js)
                    print '------------' + js + '------------'
                    fw = codecs.open(js, 'w', 'utf-8')
                    fw.write('var peopleNum={')
                    # fw.write('"%s":{' % pop_name)
                    fw.write('"peopleD":{')
                    for sqlh in range(0, 24, 1):
                        fw.write('"%d":[' % sqlh)
                        # if qybh == 'xqbh':
                        sql = "select %s,convert(int,sum(%s)/mj_gl) from population_hour_avg_popdensity where data_month='%s' and data_hour='%s' and workday = '%s' and %s!='' GROUP BY %s,mj_gl"\
                              % (qysm, pop, sqld, sqlh, wt, qysm, qysm)
                        # else:
                            # sql = "select %s,sum(%s) from population_hour_avg_jtqy where data_date='%s' and data_hour=%d  GROUP BY %s"\
                            #       % (qysm, pop, sqld, sqlh, qysm)
                            # continue
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
                            fw.write(line)
                            fw.write(',') if n < rNums else 0
                            n += 1
                        fw.write(']')
                        fw.write(',') if sqlh < 23 else 0
                    fw.write('}}')
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
    path = r'E:\data\qd_js\population_hour_avg_density'
    if conn:
        print info
        tableTransferToJson(conn, popType, sqlDate, sqlPeriod, weekType, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
