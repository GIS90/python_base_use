# -*- coding: utf-8 -*-

__author__ = 'tsnav-yangyn'

import os
import yaml
import win32event
import win32service
import win32serviceutil
#import mysql.connector
from time import sleep
from SendMsg import SendMsg
from datetime import datetime,timedelta
from logging.handlers import RotatingFileHandler



"""
GPS数据量检测程序，
白天GPS每分钟的数据量小于4000条，晚上小于200条时，向config.yaml文件中指定的号码发送报警短信
"""
def getLogger():
    import logging
    LOGFILE = os.path.abspath(os.path.join("C:\\GPSMonitor\\log", "GPSMonitor.log"))

    MAX_LOG_SIZE = 16 * 1024 * 1024
    BACKUP_COUNT = 8
    FORMAT = "%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s"
    LOG_LEVEL = 0

    handler = RotatingFileHandler(LOGFILE,
                                  mode='a',
                                  maxBytes=MAX_LOG_SIZE,
                                  backupCount=BACKUP_COUNT)

    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)

    Log = logging.getLogger()
    Log.setLevel(LOG_LEVEL)
    Log.addHandler(handler)
    return Log


#检查GPS数据量
def checkGPSNum():
    now = datetime.now()
    startTime = now - timedelta(minutes=16)
    startTime = startTime.strftime('%Y-%m-%d %H:%M:00')
    endTime = now - timedelta(minutes=15)
    endTime = endTime.strftime('%Y-%m-%d %H:%M:00')
    conn = mysql.connector.connect(host='192.168.1.77', user='qtjy', passwd='pass123', database='WS_Traffic')
    # conn = mysql.connector.connect(host='192.168.2.239', user='root', passwd='rootpass123', database='WS_Traffic')
    try:
        if conn:
            cursor = conn.cursor()
            sql = 'select count(*) from FcdT_Gps where time >= '
            sql += "'" + startTime + "'" + " and time < "
            sql += "'" + endTime + "'"
            # sql = "select count(*) from fcdt_gps1 where time >= '2014-05-14 15:00:00' and time < '2014-05-14 15:01:00'"
            cursor.execute(sql)
            gpsNum = cursor.fetchall()
            if int(gpsNum[0][0]) != 0:
                if datetime.strptime(datetime.now().strftime('%Y-%m-%d 21:00:00'),'%Y-%m-%d %H:%M:%S') > \
                datetime.now()> datetime.strptime(datetime.now().strftime('%Y-%m-%d 09:00:00'),'%Y-%m-%d %H:%M:%S'):
                    if int(gpsNum[0][0]) > 4000:
                        return 0,gpsNum[0][0]
                    else:
                        return 1,gpsNum[0][0]
                else:
                    if int(gpsNum[0][0]) > 200:
                        return 0,gpsNum[0][0]
                    else:
                        return 1,gpsNum[0][0]
            else:
                return 2,gpsNum[0][0]
    except Exception, e:
        getLogger().error('ERROR:' + str(e))
    finally:
        conn.close()



#配置文件解析
def loadConfig():
    confFile = os.path.abspath(os.path.join(os.curdir,'config.yaml'))
    assert confFile
    with open(confFile,'r') as f:
        result = yaml.load(f.read())
    phone = str(result['phone'])
    phoneList = phone.split(':')
    db = result['db']
    return phoneList, db


def Send(msg):
    phoneList, db = loadConfig()
    for phone in phoneList:
        SendMsg(phone, msg)


def GPSNumSendMsgYesOrNo():
    msg = None
    l = getLogger()
    flag, gpsNum = checkGPSNum()
    if flag == 2:
        msg = 'GPS断数异常，没有收到当前时间的GPS数据，检查时间为：' + datetime.now().strftime('%Y-%m-%d %:H%:M:%S')
    elif flag == 1:
        msg = '当前时间GPS数据量偏少，一分钟内的数据量为：' + str(gpsNum)
    else:
        log = 'GPS数据量正常，每分钟为：' + str(gpsNum)
        l.debug(log.decode('utf-8'))
    if msg:
        l.debug(msg.decode('utf-8'))
        Send(msg)


def checkConn():
    phone,db = loadConfig()
    connErrorList = []
    l = getLogger()
    for i in range(len(db['ip'])):
        try:
            conn = mysql.connector.connect(host=db['ip'][i], user=db['user'][i], passwd=db['passwd'][i])
            conn.close()
            log = '连接MySql数据库' + db['ip'][i] + '成功'
            l.debug(log.decode('utf-8'))
        except mysql.connector.errors.InterfaceError:
            connErrorList.append(db['ip'][i])
    return connErrorList


def main():
    log = getLogger()
    try:
        connErrorList = checkConn()
        # if connErrorList:
        #     msg = '连接MySql数据库失败, 不能连接的ip为：'
        #     for connError in connErrorList:
        #         msg += str(connError)
        #     log.debug(msg.decode('utf-8'))
        #     Send(msg)
        # if '192.168.1.77' not in connErrorList:
        #     GPSNumSendMsgYesOrNo()
    except Exception as e:
        log.error(str(e))


class GPSMonitorService(win32serviceutil.ServiceFramework):

    #服务名
    _svc_name_ = 'GPSMonitor'

    #显示名
    _svc_display_name_ = 'GPS数据量检测'.decode('utf-8')

    #服务描述
    _svc_description_ = 'GPS数据量检测，如果数据量达不到要求则发送短信报警'.decode('utf-8')

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = getLogger()
        self.isAlive = True

    def SvcDoRun(self):
        self.logger.debug('GPSMonitor service start')
        while self.isAlive:
            main()
            sleep(1800)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        self.logger.debug('GPSMonitor service stop')
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isAlive = False


if __name__=='__main__':
    # win32serviceutil.HandleCommandLine(GPSMonitorService)
    main()