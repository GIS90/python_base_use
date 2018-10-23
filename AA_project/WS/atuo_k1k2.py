#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    automate execute to k1, k2
    execute frequency is one on everyday 00:00:00


------------------------------------------------
"""
import datetime
import sys

import mysql.connector

DATE_FOMMAT = '%Y-%m-%d'
TIME_FOMMAT = '%Y-%m-%d %H:%M:%S'


def k1():
    pass


def k2(cursor, date):
    assert isinstance(date, basestring)

    netids = [100, 101, 201, 202, 203, 204, 205, 206]
    clas = [0, 1, 2, 5]
    hots = [1, 2]
    timeparas = "%Y-%m-%d"
    print 'k2 %s' % date
    try:
        for netid in netids:
            for cla in clas:
                for hot in hots:
                    if hot == 1:
                        sql = """
                                    insert into K2day
                                    select netid, class, CAST(date_format('%s', '%s') AS datetime) as date,
                                    CAST(avg(c1)*100 AS decimal(5, 2)) as c1,
                                    CAST(avg(c2)*100 AS decimal(5, 2)) as c2,
                                    CAST(avg(c3)*100 AS decimal(5, 2)) as c3,
                                    CAST(avg(c4)*100 AS decimal(5, 2)) as c4,
                                    CAST(avg(c5)*100 AS decimal(5, 2)) as c5, '系统计算', '1'
                                    from Total15m
                                    where time between  '%s 09:00:00' and '%s 10:30:00' and netid = %d and class = %d
                                    group by netid, class, CAST(date_format('%s', '%s') AS datetime);
                                """ % (date, timeparas, date, date, netid, cla, date, timeparas)
                    else:
                        sql = """
                                    insert into K2day
                                    select netid, class, CAST(date_format('%s', '%s') AS datetime) as date,
                                    CAST(avg(c1)*100 AS decimal(5, 2)) as c1,
                                    CAST(avg(c2)*100 AS decimal(5, 2)) as c2,
                                    CAST(avg(c3)*100 AS decimal(5, 2)) as c3,
                                    CAST(avg(c4)*100 AS decimal(5, 2)) as c4,
                                    CAST(avg(c5)*100 AS decimal(5, 2)) as c5, '系统计算', '2'
                                    from Total15m
                                    where time between  '%s 19:00:00' and '%s 20:30:00' and netid = %d and class = %d
                                    group by netid, class, CAST(date_format('%s', '%s') AS datetime);
                                """ % (date, timeparas, date, date, netid, cla, date, timeparas)

                    if cursor.execute(sql): conn.commit()
    except Exception as e:
        emsg = 'k2: %s' % e.message
        raise Exception(emsg)
    else:
        print 'k2 execute success'


def _get_curdate():
    try:
        curtime = datetime.datetime.now()
        curdate = datetime.datetime.date(curtime)
        curdate = curdate.strftime(DATE_FOMMAT)
    except Exception as e:
        print 'get current date is error: %s' % e.message
        return None
    else:
        return curdate


def _get_curtime():
    try:
        curtime = datetime.datetime.now()
        curtime = curtime.strftime(TIME_FOMMAT)
    except Exception as e:
        print 'get current time is error: %s' % e.message
        return None
    else:
        return curtime


def _get_caldate():
    try:
        curdate = _get_curdate()
        curdate = datetime.datetime.strptime(curdate, DATE_FOMMAT)
        caldate = curdate - datetime.timedelta(days=1)
    except Exception as e:
        print 'get calculated date is error: %s' % e.message
        return None
    else:
        return caldate


def main():
    config = {
        'user': 'qtjy',
        'password': 'pass123',
        'host': '192.168.1.214',
        'port': 3306,
        'database': 'WS_Traffic'}

    caldate = _get_caldate()

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
    except Exception as e:
        print 'mysql connect is error: %s' % e.message
        sys.exit(1)
    else:
        try:
            k1()
            k2(date=caldate, cursor=cursor)
        except Exception as e:
            print 'k1k2 is error: %s' % e.message
    finally:
        cursor.close()
        conn.close
        print 'end'


if __name__ == '__main__':
    print 'start'
    main()
