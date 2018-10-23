# -*- coding: utf-8 -*-

# 导包
import codecs
import datetime
import os
import pyodbc


# 获取SQLServer连接对象
def get_mssql_conn(DRIVER, server, db_default, user, password, port=1433):
    # connect函数的参数设置
    print 'Connection Information Is :'
    print 'host :', server
    print 'port :', port
    print 'user :', user
    print 'pw :', password
    print 'db :', db_default
    print 'Test Connect To SQLServer ..........'
    # 用try处理异常
    try:
        # connect连接关键字
        conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                               % (DRIVER, server, db_default, user, password)))
        if conn != -1:
            return conn, 'Connect To SQL Success !'
        else:
            return False, 'Connect To SQL Failure !'
    except Exception as e:
        print '-----Occur Exception Info :-----'
        print e.message


def table_transfer_js(conn, period, js_dir):
    assert isinstance(period, dict)
    assert isinstance(js_dir, basestring)
    if not os.path.exists(js_dir):
        os.makedirs(js_dir)
    cursor = conn.cursor()
    cursor.execute("select dday from qd_trips_period_zq GROUP BY dday")
    sql_dates = cursor.fetchall()
    for sql_date in sql_dates:
        for sqld in sql_date:
            for (key, value) in period.items():
                perKey = key
                perValue = value
                js = os.path.join(js_dir, (perKey + sqld + '.js'))
                if os.path.exists(js):
                    os.unlink(js)
                print '------------' + js + '------------'
                fw = codecs.open(js, 'w', 'utf-8')
                fw.write('var tripsData=[')
                fw.write('\n')
                sql = """
                        select leftZQSM, arrZQSM,population
                        from qd_trips_period_zq
                        where dday = '%s' and period = '%s'
                        and leftZQSM != '' and arrZQSM != ''
                        order by leftZQSM
                    """ % (sqld, perValue.decode("utf8"))
                print sql
                cursor.execute(sql)
                rows = cursor.fetchall()
                rNums = len(rows)
                print 'SQL Rows Is : %d' % rNums
                n = 1
                for row in rows:
                    leftname = row[0]
                    arrname = row[1]
                    num = int(float(row[2]))
                    line = '[{"name":"%s"},{"name":"%s","value":%s}]' % (leftname, arrname, num)
                    fw.write('\t')
                    fw.write(line)
                    fw.write(',') if n < rNums else 0
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
    DRIVER = '{SQL Server}'
    server = 'localhost'
    db_default = 'qd_db'
    user = 'sa'
    password = '123456'
    port = 1433

    conn, info = get_mssql_conn(DRIVER, server, db_default, user, password, port)

    period = {'yj': ' 夜间',
              'zgf': ' 早高峰',
              'wj': ' 晚间',
              'wgf': ' 晚高峰',
              'bt': ' 白天'}
    js_dir = r'E:\data\jd_js\zq\trips_period_zq'
    if conn:
        print info
        table_transfer_js(conn, period, js_dir)
    else:
        print info
    end_time = datetime.datetime.now()
    cost_time = (end_time - now).seconds
    print 'PyScript Cost Time Is : %s s' % cost_time