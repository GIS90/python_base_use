# coding:utf-8

import pyodbc
import codecs
import os
import datetime


# 获取SQLServer连接对象
def connSQL(connDriver, connServer, connDB, connUID, connPWD):
    print 'Test Connect To SQLServer ..........'
    # 用try处理异常
    try:
        # connect连接关键字
        conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                               % (connDriver, connServer, connDB, connUID, connPWD)))

        if conn != -1:
            print 'Connect To SQL Success !'
            return conn
        else:
            print 'Connect To SQL Failure !'
            return -1
    # 处理异常，自定义异常文件
    except Exception as e:
        print '-----Occur Exception Info :-----'
        print e.message


# 从数据库获取数据写入Json文件中
def ToEchartMapJson(conn, filePath):
    if os.path.exists(filePath):
        os.unlink(filePath)
    JsonData = []
    DataSum = 0
    f_w = codecs.open(filePath, 'w', 'utf-8')
    JsonData.append('var odData={"odo":{')
    for time in range(0, 24, 1):
        cursor = conn.cursor()
        if time < 23:
            sql_selectT1 = "select * from QD_Project.dbo.t1 where time=%s" % time
            cursor.execute(sql_selectT1)
            resultT1 = cursor.fetchall()
            JsonData.append('"%d":[' % time)
            nums = len(resultT1)
            DataSum = DataSum + nums
            n = 0
            for row in resultT1:
                n = n + 1
                id = row[0]
                startLocation = row[3]
                value = row[4]
                sql_selectT2 = "select * from QD_Project.dbo.t2 where id=%s" % id
                cursor.execute(sql_selectT2)
                resultT2 = cursor.fetchone()
                endLocation = resultT2[3]
                if (n < nums):
                    JsonData.append("[{'name':'%s'},{'name':'%s','value':'%s'}]," % (startLocation, endLocation, value))
                else:
                    JsonData.append(
                        "[{'name':'%s'},{'name':'%s','value':'%s'}]]," % (startLocation, endLocation, value))
            print 'time = %d , nums = %d' % (time, nums)
        else:
            cursor = conn.cursor()
            sql_selectT1 = "select * from QD_Project.dbo.t1 where time=%s" % time
            cursor.execute(sql_selectT1)
            resultT1 = cursor.fetchall()
            JsonData.append('"%d":[' % time)
            nums = len(resultT1)
            n = 0
            DataSum = DataSum + nums
            for row in resultT1:
                n = n + 1
                id = row[0]
                startLocation = row[3]
                value = row[4]
                sql_selectT2 = "select * from QD_Project.dbo.t2 where id=%s" % id
                cursor.execute(sql_selectT2)
                resultT2 = cursor.fetchone()
                endLocation = resultT2[3]
                if (n < nums):
                    JsonData.append("[{'name':'%s'},{'name':'%s','value':'%s'}]," % (startLocation, endLocation, value))
                else:
                    JsonData.append(
                        "[{'name':'%s'},{'name':'%s','value':'%s'}]]}}" % (startLocation, endLocation, value))
            print 'time = %d , nums = %d' % (time, nums)
    print 'Transfer To Json Sum : %d' % DataSum
    f_w.writelines(JsonData)


if __name__ == '__main__':

    print 'Start..............................................'
    print 'Ihe Python Tool Start Working !'
    startTime = datetime.datetime.now()
    print '*****Start Time : %s' % startTime
    '''
    传入之指定的参数：
        1.SQLServer的连接参数
        2.FilePath:文件的存放路径
    '''
    # connect函数的参数设置
    connDriver = '{SQL Server}'
    connServer = 'localhost'
    connDB = 'QD_Project'
    connUID = 'sa'
    connPWD = '123456'
    # 调用函数返回数据库连接对象conn
    conn = connSQL(connDriver, connServer, connDB, connUID, connPWD)
    if conn != -1:
        filePath = r"E:\connectToSDE\ceshi.json"
        # 传入conn,Json文件参数,生成json文件
        ToEchartMapJson(conn, filePath)
        print 'Ihe Python Tool Worked OK !'
        endTime = datetime.datetime.now()
        costTime = (endTime - startTime).seconds
        print '*****Cost Time : %s s' % costTime
        print 'End...............................................'
    else:
        print 'The Python Tool Abnormal End !'
