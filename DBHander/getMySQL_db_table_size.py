# coding:utf-8




import MySQLdb
import os
import arcpy
import datetime
import re
import execeptionLogging
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def getConnDB(dbHost, dbPort, dbUser, dbPw, dbDefault):
    assert isinstance(dbHost, basestring)
    assert isinstance(dbPort, int)
    assert isinstance(dbUser, basestring)
    assert isinstance(dbPw, basestring)
    assert isinstance(dbDefault, basestring)
    print 'Connection Information Is :'
    print 'host :', dbHost
    print 'port :', dbPort
    print 'user :', dbUser
    print 'pw :', dbPw
    print 'db :', dbDefault
    print 'charset :' + 'utf-8'

    try:
        dbConn = MySQLdb.Connect(host=dbHost,
                               port=dbPort,
                               user=dbUser,
                               passwd=dbPw,
                               db=dbDefault,
                               charset='utf8')
        if dbConn:
            print 'Connection MySQL Success !'
            return dbConn
        else:
            print 'Connection MySQL Failure !'
    except Exception as e:
        print e.message


def sqlResultToTxt(fPath, dbConn):
    global num
    num = 1
    cursor = dbConn.cursor()
    if os.path.exists(fPath):
        print '%s Is Exist' % fPath
    else:
        os.makedirs(fPath)




if __name__ == '__main__':
    print '***************************************'
    print 'Ihe Python Tool Working Data To MySQL !'
    startTime = datetime.datetime.now()
    print '*****Start Time :', startTime
    hostName = '127.0.0.1'
    portNum = 3306
    userName = 'root'
    pw = '123456'
    dbName = 'test'
    conn = getConnDB(hostName,
                     portNum,
                     userName,
                     pw,
                     dbName)
    if conn != -1:
        filePath = r'D:\Py_File\DBHander'
        sqlResultToTxt(filePath, conn)
        print 'Ihe Python Tool Worked OK !'
        endTime = datetime.datetime.now()
        costTime = (endTime - startTime).seconds
        print '*****Cost Time :', costTime
        print '***************************'
    else:
        print 'Python Tool Occur Exception End .'


