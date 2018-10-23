# -*- coding: utf-8 -*-

# 导包
import pyodbc
import MySQLdb
import datetime
import os
import codecs


# 获取SQLServer连接对象
def getConnDB(hostName, portNum, userName, pw, dbName):
    # connect函数的参数设置
    print 'Connection Information Is :'
    print 'host :', hostName
    print 'port :', portNum
    print 'user :', userName
    print 'pw :', pw
    print 'db :', dbName
    print 'charset :' + 'utf-8'
    try:
        conn = MySQLdb.Connect(host=hostName,
                               port=portNum,
                               user=userName,
                               passwd=pw,
                               db=dbName,
                               charset='utf8')
    # print 'Connection Information Is :'
    # print 'host :', connServer
    # print 'port :', 1433
    # print 'user :', connUID
    # print 'pw :', connPWD
    # print 'db :', connDB
    # print 'Test Connect To SQLServer ..........'
    # # 用try处理异常
    # try:
    #     # connect连接关键字
    #     conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
    #                            % (connDriver, connServer, connDB, connUID, connPWD)))
        if conn != -1:
            return conn, 'Connect To SQL Success !'
        else:
            return False, 'Connect To SQL Failure !'
    except Exception as e:
        print '-----Occur Exception Info :-----'
        print e.message

def getSQLResult(conn):
    cursor = conn.cursor()
    sql = 'select count(MemberID)  from  person'
    cursor.execute(sql)
    rows = cursor.fetchall()
    print rows[0][0]




if __name__ == '__main__':
    # 获取当前时间
    now = datetime.datetime.now()
    timeFormat = '%Y-%m-%d-%H:%m:%S%p'
    startTime = now.strftime(timeFormat)
    print 'Start Time Is : %s' % startTime
    # MySQL配置
    hostName = '192.168.2.131'
    portNum = 3306
    userName = 'root'
    pw = 'root'
    dbName = 'trip'

    # SQLServer配置
    # connDriver = '{SQL Server}'
    # connServer = 'localhost'
    # connDB = 'QD_Project'
    # connUID = 'sa'
    # connPWD = '123456'

    conn, info = getConnDB(hostName, portNum, userName, pw, dbName)

    jsonPath = r'E:\data\json\bj'
    if not os.path.exists(jsonPath):
        os.makedirs(jsonPath)
    if conn:
        print info
        getSQLResult(conn)
    else:
        print info
    endTime = datetime.datetime.now()
    costTime = (endTime - now).seconds
    print 'PyScript Cost Time Is : %s s' % costTime
