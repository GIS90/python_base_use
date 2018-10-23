# coding:utf-8

import MySQLdb
import datetime


def getConnDB(host, port, user, password, db):
    print 'Connection Information Is :'
    print 'host :', host
    print 'port :', port
    print 'user :', user
    print 'pw :', password
    print 'db :', db
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
        print e.message


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
    print conn

