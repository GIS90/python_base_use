__author__ = 'Administrator'
#coding:utf-8


'''
编程思想：
    1.获取sqlserver的connect
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
import pyodbc
import execeptionLogging
import os

#获取connect
def getConnSQLDB():

    connDriver='{SQL Server}'
    connServer='192.168.1.160'
    connDB='test'
    connUID='sa'
    connPWD='123456'
    print 'Test Connect To SQLServer ..........'
    conn=pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                         %(connDriver,connServer,connDB,connUID,connPWD)))
    if conn:
        print 'Connect To SQLServer Success !'
        return conn
    else:
        print 'Connect To SQLServer Failure !'
        return 0

#sql操作
def getProcToText(filePath,conn):
    n=0
    cursor=conn.cursor()
    tableName='sysobjects'
    sql_select='''
                select name from %s where xtype='P'
                '''%tableName
    cursor.execute(sql_select)
    procRS=cursor.fetchall()
    for pr in procRS:
        try:
            n=n+1
            rName='sde.'+str(pr).split('\'')[1]
            rTextName=rName+'.txt'
            f=os.path.join(filePath,rTextName)
            sql_exec='''
                        exec sp_helptext '%s'
                     '''%rName
            print sql_exec
            cursor.execute(sql_exec)
            fw=open(f,'w')
            textRS=cursor.fetchall()
            for trs in textRS:
                for tr in trs:
                    fw.write(str(tr))
            print 'n = %d To Text PROC Name Is : %s'%(n,rName)
        except:
            try:
                rName=str(pr).split('\'')[1]
                rTextName=rName+'.txt'
                f=os.path.join(filePath,rTextName)
                sql_exec='''
                            exec sp_helptext '%s'
                         '''%rName
                print sql_exec
                cursor.execute(sql_exec)
                fw=open(f,'w')
                textRS=cursor.fetchall()
                for trs in textRS:
                    for tr in trs:
                        fw.write(str(tr))
                print 'n = %d To Text PROC Name Is : %s'%(n,rName)
            except Exception as e:
                loggInfo=e.message
                loggType='error'
                execeptionLogging.log(loggType,loggInfo)

    cursor.close()
    conn.close()

#入口
if __name__=='__main__':

    print '***************************************'
    print 'Ihe Python Tool Working Data To SQLServer !'
    startTime=datetime.datetime.now()
    #执行调用函数
    filePath=r'E:\test\Test1211'
    try:
        conn=getConnSQLDB()
        if conn:
            #getProcToText(filePath,conn)
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

