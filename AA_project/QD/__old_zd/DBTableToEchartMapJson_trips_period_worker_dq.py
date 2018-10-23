# -*- coding: utf-8 -*-

# 导包
import codecs
import datetime
import os

import MySQLdb


# 获取SQLServer连接对象
def get_conn(db_host, db_user, db_pwd, db_default, db_port):
    # connect函数的参数设置
    print 'Connection Information Is :'
    print 'host :', db_host
    print 'port :', db_port
    print 'user :', db_user
    print 'pwd :', db_pwd
    print 'db :', db_default
    print 'Test Connect To SQLServer ..........'

    try:
        # connect连接关键字
        conn = MySQLdb.connect(db_host,
                               db_user,
                               db_pwd,
                               db_default,
                               db_port,
                               charset="utf8")
        if conn != -1:
            return conn, 'Connect To SQL Success !'
        else:
            return False, 'Connect To SQL Failure !'
    except Exception as e:
        print 'MySQLdb.connect occur eception: %s' % e.message


def table_transfer_js(conn, period, js_dir):
    assert isinstance(period, dict)
    assert isinstance(js_dir, basestring)
    if not os.path.exists(js_dir):
        os.makedirs(js_dir)
    cursor = conn.cursor()
    cursor.execute("select dday from qd_trips_period_worker_dq GROUP BY dday")
    sql_dates = cursor.fetchall()
    for sql_date in sql_dates:
        for sqld in sql_date:
            for (key, value) in period.items():
                perKey = key
                perValue = value
                sqld_new = sqld[0:4] + '-' + sqld[4:6] + '-' + sqld[6:]
                js = os.path.join(js_dir, (perKey + sqld_new + '.js'))
                if os.path.exists(js):
                    os.unlink(js)
                print '------------' + js + '------------'
                fw = codecs.open(js, 'w', 'utf-8')
                fw.write('var tripsData=[')
                fw.write('\n')
                sql = """
                        select leftDQSM, arrDQSM,population
                        from qd_trips_period_worker_dq
                        where dday = "%s" and period = "%s"
                        and leftDQBH != "NULL" and arrDQBH != "NULL"
                        order by leftDQSM
                    """ % (sqld, perValue.decode("utf8"))
                print sql
                cursor.execute(sql)
                rows = cursor.fetchall()
                rNums = len(rows)
                print 'SQL Rows Is : %d' % rNums
                n = 0
                for row in rows:
                    leftname = row[0]
                    arrname = row[1]
                    num = int(float(row[2]))
                    line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (leftname, arrname, num)
                    fw.write('\t')
                    fw.write(line)
                    fw.write(',') if n < rNums - 1 else 0
                    fw.write('\n')
                    n += 1
                fw.write(']')
                fw.close()
                print js + 'Generator Success . . . '


if __name__ == '__main__':
    # 获取当前时间
    now = datetime.datetime.now()
    time_frt = '%Y-%m-%d-%H:%m:%S%p'
    start_time = now.strftime(time_frt)
    print 'Start time is : %s' % start_time
    db_port = 3306
    db_host = '127.0.0.1'
    db_default = 'jd_db'
    db_user = 'root'
    db_pwd = '123456'

    period = {'yj': ' 夜间',
              'zgf': ' 早高峰',
              'wj': ' 晚间',
              'wgf': ' 晚高峰',
              'bt': ' 白天'}
    js_dir = r'E:\data\jd_js\dq\trips_period_worker_dq'
    conn, info = get_conn(db_host, db_user, db_pwd, db_default, db_port)
    if conn:
        print info
        table_transfer_js(conn, period, js_dir)
    else:
        print info
    end_time = datetime.datetime.now()
    cost_time = (end_time - now).seconds
    print 'PyScript Cost Time Is : %s s' % cost_time
