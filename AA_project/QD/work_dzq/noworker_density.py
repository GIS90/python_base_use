# -*- coding: utf-8 -*-

# 导包
import codecs
import datetime
import os
import pyodbc
import sys
reload(sys)
sys.setdefaultencoding('utf8')


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
        if qysm == 'zqsm':
            dir_name = 'middle'
        elif qysm == 'dqsm':
            dir_name = 'big'
        path_new = os.path.join(path, dir_name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        json = os.path.join(path_new, 'noworkerR2Density.js')
        if os.path.exists(json):
            os.unlink(json)
        print '------------' + json + '------------'
        fw = codecs.open(json, 'w', 'utf-8')
        fw.write('var noworkerR2Data=[')
        fw.write('\r\n')
        if qybh == 'zqbh':
            sql = "select %s, noworkerdensity from trips_upd_zq" % qysm
        elif qybh == 'dqbh':
            sql = "select %s, noworkerdensity from trips_upd_dq" % qysm
        print sql
        cursor.execute(sql)
        rows = cursor.fetchall()
        rNums = len(rows)
        print 'rNums : %s' % rNums
        n = 1
        for row in rows:
            name = str(row[0])
            num = int(row[1])
            fw.write('\t')
            line = '{"name":"%s","value":%d}' % (name, num)
            fw.write(line)
            fw.write(',') if n < rNums else 0
            n += 1
            fw.write('\r\n')
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
        'dqbh': 'dqsm',
        'zqbh': 'zqsm'
    }
    path = r'E:\data\qd_data_js\data\work\noworker_density'
    if conn:
        print info
        tableTransferToJson(conn, sqlJtqy, path)
    else:
        print info
    end_time = datetime.datetime.now()
    cost_time = (end_time - now).seconds

    print 'Pyscript cost time is : %s' % cost_time
