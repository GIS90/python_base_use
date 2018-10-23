# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import csv
import datetime
import inspect
import os
import sys
from datetime import timedelta

import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/21"

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class Config(object):
    startime = "2017-04-05 00:00:00"
    endtime = "2017-04-06 00:00:00"
    roadname = ["河滩快速路", "东大梁西街"]


def _get_curdir():
    if getattr(sys, 'forzen', False):
        return os.path.dirname(os.path.abspath(__file__))
    else:
        cur_dir = os.path.abspath(inspect.getfile(inspect.currentframe()))
        cur_dir = os.path.dirname(cur_dir)
        return cur_dir


# conn = MySQLdb.connect(host='192.168.2.98',
#                        user='qtjy',
#                        passwd='pass123',
#                        db="WS_Traffic",
#                        charset="utf8")
conn = MySQLdb.connect(host='192.168.1.214',
                       user='qtjy',
                       passwd='pass123',
                       db="WS_Traffic",
                       charset="utf8")
cursor = conn.cursor()

startime = datetime.datetime.strptime(Config.startime, TIME_FORMAT)
endtime = datetime.datetime.strptime(Config.endtime, TIME_FORMAT)

print 'start'
for road in Config.roadname:

    caltime = startime
    print u'query FcdT_Link05m generate %s.csv' % road
    csvpath = _get_curdir()
    csvname = u"%s.csv" % road
    csvf = os.path.join(csvpath, csvname)
    if os.path.exists(csvf):
        os.unlink(csvf)

    csvfile = file(csvf, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['time', 'name', 'speed', 'k3'])

    while True:
        if caltime > endtime:
            break

        sql = """
        select FcdT_Link05m.time as time, avg(FcdT_Link05m.speed) as speed,
        GetK3OfSpeed(linkgeo.class, avg(FcdT_Link05m.speed)) as k3
        from linkgeo LEFT JOIN FcdT_Link05m
        on linkgeo.linkid = FcdT_Link05m.linkid
        where linkgeo.roadname = "%s" and FcdT_Link05m.time = "%s"
        """ % (road, str(caltime))

        cursor.execute(sql)
        row = cursor.fetchone()
        if row[0] is not None:
            time = datetime.datetime.strftime(caltime, TIME_FORMAT)
            speed = float(row[1])
            k3 = float(row[2])
            line = [time, road, speed, k3]
            writer.writerow(line)
        else:
            time = datetime.datetime.strftime(caltime, TIME_FORMAT)
            speed = 0
            k3 = 0
            line = [time, road, speed, k3]
            writer.writerow(line)

        caltime = caltime + timedelta(minutes=5)
        # print caltime
    csvfile.close()

cursor.close()
conn.close()

print 'end'
