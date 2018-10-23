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


def table_transfer_js(conn, sql_date, work_day, js_dir):
    assert isinstance(sql_date, list)
    assert isinstance(work_day, list)
    if not os.path.exists(js_dir):
        os.makedirs(js_dir)
    cursor = conn.cursor()
    for sqld in sql_date:
        for wt in work_day:
            sqld_new = sqld[:4] + '-' + sqld[4:]
            js = os.path.join(js_dir, (wt + sqld_new + '.js'))
            if os.path.exists(js):
                os.unlink(js)
            print '------------' + js + '------------'
            fw = codecs.open(js, 'w', 'utf-8')
            fw.write('var tripsData=[')
            fw.write('\n')
            sql = """
                    select leftZQSM, arrZQSM, outlander
                    from qd_trips_outlander_zq
                    where dmonth = '%s' and workday = '%s' and
                    leftZQSM != '' and arrZQSM != ''
                    order by leftZQSM asc
                """ % (sqld, wt)
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

    conn, info = get_mssql_conn(DRIVER, server, db_default, user, password)
    sql_date = ['201509', '201510']
    work_day = ['workday', 'weekend']
    js_dir = r'E:\data\jd_js\zq\trips_outlander_zq'
    if conn:
        print info
        table_transfer_js(conn, sql_date, work_day, js_dir)
    else:
        print info
    end_time = datetime.datetime.now()
    cost_time = (end_time - now).seconds
    print 'PyScript Cost Time Is : %s s' % cost_time

