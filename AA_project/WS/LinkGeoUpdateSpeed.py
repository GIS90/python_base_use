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
import pyodbc
import time

import MySQLdb

TIME_FORMTTER = "%Y-%m-%d %H:%M:%S"
TIME_INTERNAL = 60  # seconds
SLEEP_INTERNAL = 300  # seconds
MAX_VALUE = 9999
MIN_VALUE = 0


def run():
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
            continue
        else:
            print mysql_link05m_sql
            tracuate_sql_speed = "truncate table sde.dbo.speed"
            sqls_cursor.execute(tracuate_sql_speed)
            sqls_conn.commit()
            for row in rows:
                insert_value = "(%d, %f);" % (int(row[0]), float(row[1]))
                sqls_insert = "insert into sde.dbo.speed values" + insert_value
                sqls_cursor.execute(sqls_insert)
                sqls_conn.commit()
            tracuate_sql_link = "update sde.dbo.ws_link set speed = 0"
            sqls_cursor.execute(tracuate_sql_link)
            sqls_conn.commit()
            sqls_update = """
                            UPDATE sde.dbo.ws_link
                            SET sde.dbo.ws_link.speed = sde.dbo.speed.speed
                            FROM
                            sde.dbo.ws_link
                            LEFT JOIN sde.dbo.speed ON sde.dbo.ws_link.LinkId = sde.dbo.speed.LinkId
                          """
            sqls_cursor.execute(sqls_update)
            sqls_conn.commit()

            mysql_cursor.close()
            mysql_conn.close()
            sqls_cursor.close()
            sqls_conn.close()


if __name__ == "__main__":

    print "====================================Start===================================="
    while True:
        run()
        time.sleep(TIME_INTERNAL)
