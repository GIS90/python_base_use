# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import datetime
import pymssql
import sys
from collections import namedtuple

import mysql.connector

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/1/12"

TIME_FROMAT = "%Y-%m-%d %H:%M:%S"

DB = namedtuple('DB', ['type', 'host', 'user', 'password', 'port', 'database', 'charset'])
mysql_config = DB('mysql', '192.168.2.98', 'root', 'rootpass123', 3306, 'TY_Traffic', 'utf8')
mssql_config = DB('sqlserver', '192.168.2.163', 'sa', '123456', 1433, 'TY_SDE', 'utf8')


def get_link_k3(cal_time):
    config = {
        'host': mysql_config.host,
        'user': mysql_config.user,
        'password': mysql_config.password,
        'port': mysql_config.port,
        'database': mysql_config.database,
        'charset': mysql_config.charset
    }
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        if not cursor:
            emsg = "mysql connect db is connect failure: %s" % e.message
            raise Exception(emsg)
    except mysql.connector.Error as e:
        emsg = "mysql connect db is connect error: %s" % e.message
        raise Exception(emsg)
    except Exception as e:
        emsg = "mysql connect db is error: %s" % e.message
        raise Exception(emsg)

    sql_calk3 = """
            select a.linkid,
                round(case
                    when a.speed > c.b0 + 20 then 0
                    when a.speed > c.b0 then 2*(speed-b0)/20
                    when a.speed > c.b1 then 2+2*(speed-b1)/(b0-b1)
                    when a.speed > c.b2 then 4+2*(speed-b2)/(b1-b2)
                    when a.speed > c.b3 then 6+2*(speed-b3)/(b2-b3)
                    else 8+2*speed/b3 end, 4) as k3
                from FcdT_Link05m a
                join Link b on a.linkid=b.linkid
                left join K2Ref c on b.Class=c.c
                where a.time = '%s';
            """ % cal_time
    try:
        cursor.execute(sql_calk3)
        rows = cursor.fetchall()
        print "mysql cal k3 count: %d" % cursor.rowcount
    except Exception as e:
        emsg = 'mysql query k3 is error: %d' % e.message
        raise Exception(emsg)
    else:
        cursor.close()
        conn.close()
        return list(rows) if rows else None


def update_link_k3(rows):
    assert isinstance(rows, list)

    try:
        conn = pymssql.connect(server=mssql_config.host,
                               user=mssql_config.user,
                               password=mssql_config.password,
                               database=mssql_config.database,
                               timeout=20,
                               login_timeout=20,
                               charset=mssql_config.charset,
                               as_dict=False,
                               port=mssql_config.port,
                               autocommit=True)
        cursor = conn.cursor()
        if not cursor:
            emsg = "mssql connect db is connect failure: %s" % e.message
            raise Exception(emsg)
    except pymssql.Error as e:
        emsg = "mssql connect db is connect error: %s" % e.message
        raise Exception(emsg)
    except Exception as e:
        emsg = "mssql connect db is error: %s" % e.message
        raise Exception(emsg)

    sql_trtk3 = 'TRUNCATE table linkgeo_k3;'
    sql_insk3 = "INSERT INTO linkgeo_k3 VALUES(%d, %f)"
    sql_uptk3 = """
                    UPDATE linkgeo
                    SET linkgeo.k3 = linkgeo_k3.k3
                    FROM linkgeo
                    LEFT JOIN linkgeo_k3 ON linkgeo.LinkId = linkgeo_k3.LinkId
                """
    try:
        cursor.execute(sql_trtk3)
        conn.commit()
    except Exception as e:
        emsg = "mssql db truncate k3 is error: %s" % e.message
        raise Exception(emsg)
    for row in rows:
        try:
            sql = sql_insk3 % (int(row[0]), float(row[1]))
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            emsg = "mssql db %d insert k3 is error: %s" % (row[0], e.message)
            raise Exception(emsg)
    try:
        cursor.execute(sql_uptk3)
        conn.commit()
    except Exception as e:
        emsg = "mssql db update k3 is error: %s" % e.message
        raise Exception(emsg)
    else:
        print 'mssql update k3 count: %d' % cursor.rowcount
        cursor.close()
        conn.close()


def main():
    cur_time = datetime.datetime.now().strftime(TIME_FROMAT)
    print 'start update mssql %s linkgeo k3' % cur_time
    t = '2016-08-22 16:20:00'
    try:
        k3_rows = get_link_k3(t)
        if k3_rows:
            update_link_k3(k3_rows)
        else:
            print 'update linkgeo k3 failure'
            sys.exit(0)
    except Exception as e:
        print 'update linkgeo k3 failure: %s' % e.message

    print 'update linkgeo k3 success'


if __name__ == '__main__':
    main()
