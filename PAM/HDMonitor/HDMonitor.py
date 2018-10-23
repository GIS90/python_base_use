# -*- coding: utf-8 -*-


import win32serviceutil
import win32service
import win32event
from logging.handlers import RotatingFileHandler
from collections import namedtuple
import os
import yaml
import time
from datetime import datetime
from Util import *


PATH_INFO = namedtuple("PATH_INFO", "path timedelta")


def getLogger():
    import logging
    import inspect
    thisFile = inspect.getfile(inspect.currentframe())
    thisFolder = os.path.abspath(os.path.dirname(thisFile))
    LOGFILE = os.path.abspath(os.path.join("C:\\HDMonitor", "HDMonitor.log"))

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


def getPathList(logger):
    DIR = os.path.abspath(os.path.dirname(__file__))
    yamlFile = os.path.abspath(os.path.join(DIR, "config.yaml"))
    if not os.path.exists(yamlFile):
        logger.debug("getPathList yamlfile not exist " + yamlFile)
        return
    retval = []
    with open(yamlFile) as f:
        try:
            result = yaml.load(f.read())
            if "paths" in result:
                paths = result['paths']
                if isinstance(paths, list) and len(paths):
                    for item in paths:
                        v = item.values()[0]
                        path = v['path']
                        timedelta = int(v['timedelta'])
                        p = PATH_INFO(path, timedelta)
                        retval.append(p)
        except Exception, e:
            logger.error("getPathList got exception, error is " + str(e))
    return retval


class HDMonitorService(win32serviceutil.ServiceFramework):
    """
    Usage: 'HDMonitor.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
    Options for 'install' and 'update' commands only:
     --username domain\username : The Username the service is to run under
     --password password : The password for the username
     --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
     --interactive : Allow the service to interact with the desktop.
     --perfmonini file: .ini file to use for registering performance monitor data
     --perfmondll file: .dll file to use when querying the service for
       performance data, default = perfmondata.dll
    Options for 'start' and 'stop' commands only:
     --wait seconds: Wait for the service to actually start or stop.
                     If you specify --wait with the 'stop' option, the service
                     and all dependent services will be stopped, each waiting
                     the specified period.
    注意
    _svc_name_、_svc_display_name_、_svc_description_、__init__、SvcDoRun、SvcStop都是ServiceFramework
    内置的方法，只能重写，不要改名，否则框架无法识别，导致启动失败！！！！！

    """
    # 服务名
    _svc_name_ = "HDMonitorService"

    # 服务显示名称
    _svc_display_name_ = "硬盘空间监控".decode("utf-8")

    # 服务描述
    _svc_description_ = "定期主动释放历史文件".decode("utf-8")

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = getLogger()
        self.isAlive = True
        self.logger.error("before getPathList")
        self.paths = getPathList(self.logger)
        for p in self.paths:
            path = p.path
            timedelta = p.timedelta
            self.logger.debug("we will monitor the folder " + str(path) + " at interval " + str(timedelta))
        self.logger.error("after getPathList")

    def SvcDoRun(self):
        self.logger.debug("HDMonitor svc start")
        while self.isAlive:
            try:
                for p in self.paths:
                    path = p.path
                    timedelta = p.timedelta
                    self.deleteFilesIfTimeout(path, timedelta)
            except Exception, e:
                self.logger.error("SvcDoRun got exception, error is " + str(e))
            finally:
                time.sleep(5)
        # 等待服务被停止
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        self.logger.error("HDMonitor svc stop")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # 设置事件
        win32event.SetEvent(self.hWaitStop)
        self.isAlive = False

    def deleteFilesIfTimeout(self, path, timeout):
        if not os.path.exists(path):
            self.logger.debug("deleteFilesIfTimeout folder not exist " + path)
            return
        # self.logger.debug("deleteFilesIfTimeout we will monitor the path " + path + "\t" + str(timeout))
        try:
            paths = self.getTimeoutFiles(path, timeout)
            for p in paths:
                if removePath(p):
                    self.logger.debug("deleteFilesIfTimeout we delete file " + str(p) + " success")
        except Exception, e:
            self.logger.error("deleteFilesIfTimeout got exception " + str(e))

    def getTimeoutFiles(self, path, timeout):
        """
        获取path下的最后一次修改时间在timeout之前的文件信息，如果path是一个文件，则检查path的最后一次修改时间是否大于timeout
        :param path: 指定的文件或目录
        :param timeout: 超时的时间，单位秒
        :return:
        """
        retval = []
        now = datetime.now()
        try:
            if os.path.isfile(path):
                ct = time.ctime(os.path.getmtime(path))
                d = datetime.strptime(ct, "%a %b %d %H:%M:%S %Y")
                if (now - d).seconds > timeout:
                    retval.append(path)
            elif os.path.isdir(path):
                files = os.listdir(path)
                for f in files:
                    filePath = os.path.abspath(os.path.join(path, f))
                    ct = time.ctime(os.path.getctime(filePath))
                    d = datetime.strptime(ct, "%a %b %d %H:%M:%S %Y")
                    if (now - d).seconds > timeout:
                        self.logger.debug("getTimeoutFiles we will try to delete file " + filePath)
                        retval.append(filePath)
        except Exception, e:
            self.logger.error("getTimeoutFiles got exception, error is " + str(e))
        finally:
            return retval


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(HDMonitorService)
