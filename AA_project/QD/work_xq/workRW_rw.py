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


def tableTransferToJson(conn, work, path):
    assert isinstance(work, dict)
    for wbh, rbh in work.items():
        if wbh == 'wxqbh':
            name = 'smaller'
        elif wbh == 'wzqbh':
            name = 'middle'
        elif wbh == 'wdqbh':
            name = 'big'
        path_new = os.path.join(path, name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        js = os.path.join(path_new, 'workRW.js')
        fw = codecs.open(js, 'w', 'utf-8')
        fw.write('var workRWData={')
        fw.write('\r\n')
        fw.write('\t')
        fw.write("'Data':[")
        fw.write("\n")
        cursor = conn.cursor()
        if wbh == "wxqbh":
            sql = """
                select g1.sm, g1.wworker, g2.rworker from
                (select sum(qd_workerRW.workder) as wworker, qd_workerRW.wxqsm as sm ,qd_workerRW.wxqbh
                from qd_workerRW
                GROUP BY qd_workerRW.wxqsm, qd_workerRW.wxqbh) g1,
                (select sum(qd_workerRW.workder) as rworker, qd_workerRW.rxqsm as sm ,qd_workerRW.rxqbh
                from qd_workerRW
                GROUP BY qd_workerRW.rxqsm, qd_workerRW.rxqbh) g2
                WHERE g1.wxqbh = g2.rxqbh
            """
        elif wbh == "wzqbh":
            sql = """
                select g1.sm, g1.wworker, g2.rworker from
                (select sum(qd_workerRW.workder) as wworker, qd_workerRW.wzqsm as sm ,qd_workerRW.wzqbh
                from qd_workerRW
                GROUP BY qd_workerRW.wzqsm, qd_workerRW.wzqbh) g1,
                (select sum(qd_workerRW.workder) as rworker, qd_workerRW.rzqsm as sm ,qd_workerRW.rzqbh
                from qd_workerRW
                GROUP BY qd_workerRW.rzqsm, qd_workerRW.rzqbh) g2
                WHERE g1.wzqbh = g2.rzqbh
            """
        elif wbh == "wdqbh":
            sql = """
                select g1.sm, g1.wworker, g2.rworker from
                (select sum(qd_workerRW.workder) as wworker, qd_workerRW.wdqsm as sm ,qd_workerRW.wdqbh
                from qd_workerRW
                GROUP BY qd_workerRW.wdqsm, qd_workerRW.wdqbh) g1,
                (select sum(qd_workerRW.workder) as rworker, qd_workerRW.rdqsm as sm ,qd_workerRW.rdqbh
                from qd_workerRW
                GROUP BY qd_workerRW.rdqsm, qd_workerRW.rdqbh) g2
                WHERE g1.wdqbh = g2.rdqbh
            """
        print 'sql : %s' % sql
        cursor.execute(sql)
        rows = cursor.fetchall()
        n = 1
        rNums = len(rows)
        print 'rNums : %d' % rNums
        for row in rows:
            name = row[0]
            wnum = row[1]
            rnum = row[2]
            rlt = float(wnum / rnum)
            fw.write('\t')
            line = '{"name":"%s","value":%.2f}' % (name, rlt)
            fw.write(line)
            fw.write(',') if n < rNums else fw.write(']')
            n += 1
            fw.write('\r\n')
        fw.write('}')
        fw.close()


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
    path = r'E:\data\qd_data_js\data\work\workRW_rw'
    work = {
        'wxqbh': 'rxqbh',
        # 'wdqbh': 'rdqbh',
        # 'wzqbh': 'rzqbh'
    }
    if conn:
        print info
        tableTransferToJson(conn, work, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
