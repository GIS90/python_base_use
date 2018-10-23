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

def tableTransferToJson(conn, work, path):
    assert isinstance(work, dict)
    for qybh,qysm in work.items():
        if qybh == 'xqbh':
            name = 'smaller'
        elif qybh == 'zqbh':
            name = 'minddle'
        elif qybh == 'dqbh':
            name = 'big'
        path_new = os.path.join(path, name)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        js = os.path.join(path_new, 'workRW.js')
        fw = codecs.open(js, 'w', 'utf-8')
        fw.write('var workRWData={')
        fw.write('\r\n')
        fw.write('\t')
        flag = 1
        for work in qysm:
            if work == 'rxqsm' or work == 'rdqsm' or work == 'rzqsm':
                fw.write("'RData':[")
                fw.write('\r\n')
            else:
                fw.write('\t')
                fw.write("'WData':[")
                fw.write('\r\n')
            cursor = conn.cursor()
            # if work == 'rxqsm' or 'wxqsm':
            #     sql = 'select %s,sum(workder) from workerRW_jtqy group by %s' % (work, work)
            # else:
            #     sql = 'select %s,sum(workder) from workerRW_jtqy group by %s' % (work, work)
            if work == 'rxqsm' or work == 'rdqsm' or work == 'rzqsm':
                sql = 'select %s,convert(int,sum(workder)/rmj_gl) from workerRW_popdensity group by %s,rmj_gl' % (work, work)
                print 'sql : %s' % sql
            else:
                 sql = 'select %s,convert(int,sum(workder)/wmj_gl) from workerRW_popdensity group by %s,wmj_gl' % (work, work)
                 print 'sql : %s' % sql
            cursor.execute(sql)
            rows = cursor.fetchall()
            n = 1
            rNums = len(rows)
            print 'rNums : %d' % rNums
            for row in rows:
                name = row[0]
                num = row[1]
                fw.write('\t')
                line = '{"name":"%s","value":%s}' % (name, num)
                fw.write(line)
                if flag == 1:
                    fw.write(',') if n < rNums else fw.write('],')
                else:
                    fw.write(',') if n < rNums else fw.write(']')
                n += 1
                fw.write('\r\n')
            flag = flag + 1
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
    connDB = 'qd_js'
    connUID = 'sa'
    connPWD = '123456'
    conn, info = getConnDB(connDriver, connServer, connDB, connUID, connPWD)
    path = r'E:\data\qd_js\workerRW_density'
    work = {
        'xqbh': ['rxqsm', 'wxqsm'],
        # 'dqbh': ['rdqsm', 'wdqsm'],
        # 'zqbh': ['rzqsm', 'wzqsm']
    }
    if conn:
        print info
        tableTransferToJson(conn, work, path)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s' % costTime
