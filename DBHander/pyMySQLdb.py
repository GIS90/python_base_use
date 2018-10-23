# coding:utf-8

import datetime
import os
import re
import sys

import MySQLdb
import arcpy
import execeptionLogging

reload(sys)
exec ("sys.setdefaultencoding('utf-8')")


def getConnDB(hostName, portNum, userName, pw, dbName):
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
        if conn:
            print 'Connection MySQL Success !'
            return conn
        else:
            print 'Connection MySQL Failure !'
    except Exception as e:
        logInfo = e.message
        logType = 'error'
        execeptionLogging.log(logType, logInfo)


def txtToMySQL(filePath, conn):
    global num
    num = 1
    cursor = conn.cursor()
    if os.path.exists(filePath):
        print '%s Is Exist' % filePath
        arcpy.env.workspace = filePath
        for fileName in arcpy.ListFiles('*.txt'):
            print '%s-------------------' % fileName
            fileText = os.path.join(filePath, fileName)
            fOpen = open(fileText, 'r')
            fLines = fOpen.readlines()
            for fLine in fLines:
                reg = '\d'
                pattern = re.compile(reg)
                match = re.match(pattern, fLine)
                if match:
                    contentLine = fLine.decode('utf-8').split(',')
                    id = int(contentLine[0])
                    _Custom2 = str(contentLine[1])
                    _carnum = str(contentLine[2])
                    _direction = int(contentLine[3])
                    _gpstime = str(contentLine[4])
                    _isalarm = int(contentLine[5])
                    _lat = float(contentLine[6])
                    _lon = float(contentLine[7])
                    _speed = float(contentLine[8])

                    sql_insert = "insert into gps values('%d','%s','%d','%s',%d,%f,%f,%f)" % (
                        id, _carnum, _direction, _gpstime, _isalarm, _lat, _lon, _speed)
                    print sql_insert
                    try:
                        cursor.execute(sql_insert)
                        conn.commit()
                        print '%d Row Data Insert into GPS Success !' % num
                        num = num + 1
                    except Exception as e:
                        print 'e:' + e.message
                        logInfo = e.message
                        logType = 'error'
                        execeptionLogging.log(logType, logInfo)

                else:
                    pass
            print '%s Execute To MySQL Ok' % fileName
        cursor.close()
        conn.close()
        print 'Data SUM %d All Data Runned OK !' % num


    else:
        print '%s Is Not Exist' % filePath


if __name__ == '__main__':
    print '***************************************'
    print 'Ihe Python Tool Working Data To MySQL !'
    startTime = datetime.datetime.now()
    print '*****Start Time :', startTime
    hostName = '127.0.0.1'
    portNum = 3336
    userName = 'root'
    pw = '123456'
    dbName = 'test'
    conn = getConnDB(hostName,
                     portNum,
                     userName,
                     pw,
                     dbName)
    print conn
    filePath = r'E:\2015Project'
    # txtToMySQL(filePath, conn)

    print 'Ihe Python Tool Worked OK !'
    endTime = datetime.datetime.now()
    costTime = (endTime - startTime).seconds
    print '*****Cost Time :', costTime
    print '***************************'
