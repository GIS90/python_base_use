#coding:utf-8



import MySQLdb
import datetime




def getConnDB(hostName,portNum,userName,pw,dbName):

    print 'Connection Information Is :'
    print 'host :',hostName
    print 'port :',portNum
    print 'user :',userName
    print 'pw :',pw
    print 'db :',dbName
    print 'charset :'+'utf-8'

    try:
        conn=MySQLdb.Connect(host=hostName,
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
            print e.message

def exeProcK1(conn):
    formatTime='%Y-%m-%d'
    cursor=conn.cursor()
    nowTime=datetime.datetime.now()
    tStart=(nowTime+datetime.timedelta(days=-1)).strftime(formatTime)
    tEnd=(nowTime).strftime(formatTime)
    print tStart,tEnd
    sql_Proc="call K1DaySaver('%s','%s')"%(tStart,tEnd)
    try:
        cursor.execute(sql_Proc)
        conn.commit()
        print 'Execute K1DaySaver Success !'
    except Exception as e:
        print 'Execute K1DaySaver Failure !'
        print e.message



if __name__=='__main__':

    print '**************************************************'
    print 'Ihe Python Tool Working Data To MySQL !'
    hostName='192.168.1.214'
    portNum=3306
    userName='qtjy'
    pw='pass123'
    dbName='WS_Traffic'
    conn=getConnDB(hostName,
                   portNum,
                   userName,
                   pw,
                   dbName)
    startTime=datetime.datetime.now()
    print '*****, Start Time : %s,'%startTime
    exeProcK1(conn)
    endTime=datetime.datetime.now()
    costTime=(endTime-startTime).seconds
    print '*****Exe K1DayServer OK , Cost Time :',costTime
    print '**************************************************'