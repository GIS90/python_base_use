# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: LinkGeoUpdateSpeed.py
@time: 2016/10/12 11:35
@describe: The FcdT_Link05m of 31 MySQL update to ws_link in 83 SQL Server
            5 minute to update once
@remark: single thread
------------------------------------------------
"""
import datetime
import os
import pyodbc
import time
import win32event
import win32service

import MySQLdb
import win32serviceutil

TIME_FORMTTER = "%Y-%m-%d %H:%M:%S"
LOG_FROMTTER = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
LOG_NAME = "LinkgeoUpSpeedSev.log"
TIME_INTERNAL = 60  # seconds
SLEEP_INTERNAL = 60 * 13  # seconds
MAX_VALUE = 9999
MIN_VALUE = 0


class PyService(win32serviceutil.ServiceFramework):
    # service infos
    __svc_name_ = "LinkgeoUpSpeedSev"
    __svc_display_name_ = "LinkgeoUpSpeedSev"
    __svc_description_ = "The FcdT_Link05m of 31 MySQL update to ws_link "
    __svc_description_ += __svc_description_ + "in 83 SQL Server 5 minute to update once"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.isLive = True
        self.logger = __getlog()

    def __getlog(self):
        import logging
        import inspect

        logger = logging.getLogger("PyService")
        cur_dir = inspect.getfile(inspect.currentframe())
        log_dir = os.path.abspath(cur_dir)

        handler = logging.FileHandler(os.path.join(log_dir, LOG_NAME))
        formatter = logging.Formatter(LOG_FROMTTER)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    def SvcStop(self):
        self.logger.error("%s is occur error" % self.__svc_display_name_)
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isLive = False

    def SvcDoRun(self):
        self.logger.error("====================================Start====================================")
        while self.isLive:
            self.update()
        else:
            win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def update(self):
        mysql_conn = MySQLdb.connect(host='192.168.1.214', user='qtjy', passwd='pass123', db="WS_Traffic", charset="utf8")
        mysql_cursor = mysql_conn.cursor()
        sqls_conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                                    % ("{SQL Server}", "localhost", "sde", "sa", "itswork.2014")))
        sqls_cursor = sqls_conn.cursor()

        now = datetime.datetime.now()
        secn = 0
        while True:
            secn += 1
            query_time = now - datetime.timedelta(seconds=TIME_INTERNAL * secn)
            query_time = query_time.strftime(TIME_FORMTTER)
            query_time = query_time[:-2] + "00"
            mysql_link05m_sql = 'select linkid, speed from FcdT_Link15m where time = "%s"' % query_time
            mysql_cursor.execute(mysql_link05m_sql)
            rows = mysql_cursor.fetchall()
            if not rows:
                time.sleep(TIME_INTERNAL)
                continue
            else:
                self.logger.error(mysql_link05m_sql)
                for row in rows:
                    insert_value = "(%d, %f);" % (int(row[0]), float(row[1]))
                    sqls_insert = "insert into sde.dbo.speed values" + insert_value
                    print sqls_insert
                    sqls_cursor.execute(sqls_insert)
                    sqls_conn.commit()
                sqls_update = """
                                UPDATE sde.dbo.ws_link
                                SET sde.dbo.ws_link.speed = sde.dbo.speed.speed
                                FROM
                                sde.dbo.ws_link
                                LEFT JOIN sde.dbo.speed ON sde.dbo.ws_link.LinkId = sde.dbo.speed.LinkId
                              """
                print sqls_update
                sqls_cursor.execute(sqls_update)
                sqls_conn.commit()
                time.sleep(SLEEP_INTERNAL)
                break
        mysql_conn.close()
        mysql_cursor.close()
        sqls_conn.close()
        sqls_cursor.close()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PyService)
