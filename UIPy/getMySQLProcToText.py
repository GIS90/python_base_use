__author__ = 'Administrator'
#coding:utf-8


'''
编程思想：
    1.获取sMySQL的connect
    2.查询所有的proc名称
    3.遍历proc名称
    4.对获取的每一个proc名称进行helptext
    5.将返回的text存成文本放在硬盘上
    注：1.遍历sde数据库是，执行exec sp_helptext rName,rName有时需要带sde前缀，有时不带，
    情况不定，暂时没有找到条件确定是否带sde,只能通过异常处理，先try带sde，发生异常，不带sde
    2.经测试，获取不了加密的存储过程（with encryption）
'''

#导包
import datetime
import MySQLdb
import execeptionLogging
import os

#获取connect
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

        return conn


    except Exception as e:
        loggInfo=e.message
        loggType='error'
        execeptionLogging.log(loggType,loggInfo)


#sql操作
def getProcToText(filePath,conn):
    n=0
    cursor=conn.cursor()
    sql_select='''
                show procedure status
                '''
    cursor.execute(sql_select)
    procRS=cursor.fetchall()
    for pr in procRS:
        print pr


    cursor.close()
    conn.close()

#入口
if __name__=='__main__':

    print '***************************************'
    print 'Ihe Python Tool Working Data To MySQL !'
    startTime=datetime.datetime.now()
    #执行调用函数
    filePath=r'E:\test\Test1211'
    hostName='127.0.0.1'
    portNum=3306
    userName='root'
    pw='123456'
    dbName='sde'
    try:
        conn=getConnDB(hostName,
                   portNum,
                   userName,
                   pw,
                   dbName)
        if conn:
            getProcToText(filePath,conn)
            print 'Ihe Python Tool Worked OK !'
        else:
            exit()
    #自定义打印异常
    except Exception as e:
        loggInfo=e.message
        loggType='error'
        execeptionLogging.log(loggType,loggInfo)
    endTime=datetime.datetime.now()
    print '*****Cost Time : %s'%((endTime-startTime).seconds)
    print '***************************************'

