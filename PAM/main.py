# -*- coding: utf-8 -*-

# 程序入口，通过多线程并发查询每台服务器
import os
import Queue
from time import sleep
from threading import Thread
from datetime import datetime, timedelta
from core.Log import Log
from core.SQLHandle import SQLHandle
from core.DBHandler import DBHandler
from core.SendDataYunHost import TCPClient
from core.HDStorage import getRemoteHDUsageBySNMP
from core.Process import isRemoteProcessAliveBySNMP
from core.YAMLLoader import loadDevYaml, loadMasterYaml

q = Queue.Queue()


class checkDevThread(Thread):
    """
    需要传入配置文件名和所在区域
    """

    def __init__(self, confFile, area):
        Thread.__init__(self)
        self.confFile = confFile
        self.area = area.encode('utf-8')
        self.now = datetime.now()
        self.dataList = []

    def run(self):
        Log.debug('启动一个新的线程，根据' + self.confFile + '文件')
        self.getCheckResult()
        Log.debug(self.confFile + '文件的线程已完成')

    def getCheckResult(self):
        """
        获取配置文件中要得到的信息，并按一定的格式将所有信息整合到列表中，之后之后添加到队列中
        :return: 无返回值
        """
        devIp, devOsType, devCf, devCheckItem = loadDevYaml(self.confFile)
        Log.debug('开始检查' + devIp)
        for attr in devCheckItem:
            try:
                value = devCheckItem[attr]
                attr = attr.lower()
                if attr == 'process':
                    for ps in value:
                        process = ps['cmd']
                        program = process.split()[0]
                        cmdList = ' '.join(process.split()[1:])
                        flag, cmd, stat = isRemoteProcessAliveBySNMP(devIp, devCf['snmp'].comm, devCf['snmp'].port,
                                                                     program, cmdList)
                        data = (' ', self.now.strftime('%Y-%m-%d %H:%M:%S'), self.area, devIp, devOsType, attr, ps['description'],
                                stat, cmd, flag)
                        Log.debug(data[2:])
                        self.dataList.append(data)
                elif attr == 'hd':
                    hdInfo = getRemoteHDUsageBySNMP(devIp, comm=devCf['snmp'].comm, port=devCf['snmp'].port)
                    for conf in value:
                        for hdData in hdInfo:
                            confHd = [item.replace("\\", "") for item in conf['path']]
                            snmpHd = [item.replace("\\", "") for item in hdData.driver]
                            confHd = ''.join(confHd)
                            snmpHd = ''.join(snmpHd)
                            if confHd == snmpHd or confHd + ' ' == snmpHd:
                                if hdData.percent > conf['warnning']:
                                    msg = hdData.driver + '本硬盘目录作用：' + conf['description'] + '请及时清理硬盘'
                                    data = (' ', self.now.strftime('%Y-%m-%d %H:%M:%S'), self.area, devIp, devOsType, attr,
                                            hdData.driver, hdData.percent, msg, 1)
                                else:
                                    msg = hdData.driver + '本硬盘目录作用：' + conf['description'] + '硬盘空间充足'
                                    data = (' ', self.now.strftime('%Y-%m-%d %H:%M:%S'), self.area, devIp, devOsType,
                                            attr, hdData.driver, hdData.percent, msg, 0)
                                Log.debug(data[2:])
                                self.dataList.append(data)
                elif attr == 'db':
                    dbInfo = devCf['db']
                    if dbInfo.enable == 1:
                        for checkDb in value:
                            db = DBHandler(dbInfo.dbtype, devIp, dbInfo.port, dbInfo.user, dbInfo.password,
                                           checkDb['dbName'])
                            queryResult = db.query(checkDb['sql'], 1)
                            tableName = checkDb['sql'].lower().split('from')[1].split()[0]
                            startTime = datetime.strptime(queryResult, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=60)
                            endTime = queryResult
                            countSql = 'select count(*) from ' + tableName + ' where time between ' + "'" +str(
                                startTime) + "'" + ' and ' + "'" + str(endTime) + "'"
                            count = db.query(countSql, 1)
                            if self.now - timedelta(seconds=checkDb['delay']) > datetime.strptime(queryResult, '%Y-%m-%d %H:%M:%S'):
                                msg = '当前时间数据库已经断数，数据库中最后一条记录的时间为：'
                                msg += str(queryResult) + '，请检查数据库'
                                data = (' ', self.now.strftime('%Y-%m-%d %H:%M:%S'), self.area, devIp, devOsType,
                                        attr, checkDb['alias'], 0, msg, 1)
                            else:
                                msg = '当前时间数据库中一分钟的数据量为：' + str(count)
                                data = (' ', self.now.strftime('%Y-%m-%d %H:%M:%S'), self.area, devIp, devOsType,
                                        attr, checkDb['alias'], count, msg, 0)
                            Log.debug(data[2:])
                            self.dataList.append(data)
                            db.close()
            except Exception, e:
                msg = '获取信息时发生错误，错误信息为：' + str(e)
                Log.error(msg)
                data = (' ', self.now.strftime('%Y-%m-%d %H:%M:%S'), self.area, devIp, devOsType, '系统', 'Server', 0, msg, 1)
                self.dataList.append(data)
        Log.debug(devIp + '检查完成')
        q.put(self.dataList)


def Server():
    """
    主函数，根据设备配置文件的个数决定开启几个线程，同时检查每台设备，
    之后将检查结果转换成sql语句，发送到云服务器
    :return: 无
    """
    allInfo = []
    thList = []
    allDevDataList = []
    sendTo = step = area = None
    try:
        sendTo, step, area = loadMasterYaml()
        confDir = os.path.abspath(os.path.join(os.curdir, 'config'))
        confList = os.listdir(confDir)
        for confFile in confList:
            if confFile.lower() in ['master.yaml', 'default_dev.yaml']:
                continue
            checkThread = checkDevThread(confFile, area)
            thList.append(checkThread)
            checkThread.start()
        for th in thList:
            th.join()
        while not q.empty():
            allInfo.append(q.get())
        for thInfo in allInfo:
            for itemInfo in thInfo:
                allDevDataList.append(itemInfo)
        sql = SQLHandle(allDevDataList)
        print sql
        pushData = TCPClient(sendTo.ip, sendTo.port)
        pushData.sendMsg(sql)
    except Exception, e:
        errorMsg = '主函数运行错误，错误为：' + str(e)
        Log.error(errorMsg)
        errorTuple = (' ', datetime.now(), area.encode('utf-8'), '跳转机主函数错误', os.name, 'PAM', 'script', 0, errorMsg, 1)
        errorList = [errorTuple]
        sqlPAM = SQLHandle(errorList)
        push = TCPClient(sendTo.ip, sendTo.port)
        push.sendMsg(sqlPAM)
    finally:
        sleep(step)


if __name__ == '__main__':
    Server()