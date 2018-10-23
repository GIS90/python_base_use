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
        if conn:
            return conn, 'Connect To SQL Success !'
        else:
            return False, 'Connect To SQL Failure !'
    except Exception as e:
        print '-----Occur Exception Info :-----'
        print e.message


def tableTransferToJson(conn, sqlJtqy, path):
    assert isinstance(sqlJtqy, dict)
    cursor = conn.cursor()
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
        json = os.path.join(path_new, 'popdens.js')
        if os.path.exists(json):
            os.unlink(json)
        print '------------' + json + '------------'
        fw = codecs.open(json, 'w', 'utf-8')
        fw.write('var peopleNum=[')
        if qybh == 'xqbh':
            sql = "select %s, population from popdensity_xq" % qysm
        elif qybh == 'zqbh':
            sql = "select %s, population from popdensity_zq" % qysm
        elif qybh == 'dqbh':
            sql = "select %s, population from popdensity_dq" % qysm
        print sql
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

    sqlJtqy = {
        'xqbh': 'xqsm',
        'dqbh': 'dqsm',
        'zqbh': 'zqsm'
    }
    path = r'E:\data\qd_data_js\data\population_density\population_density'
    if conn:
        print info
        tableTransferToJson(conn, sqlJtqy, path)
    else:
        print info
    end_time = datetime.datetime.now()
    cost_time = (end_time - now).seconds

    print 'Pyscript cost time is : %s' % cost_time
