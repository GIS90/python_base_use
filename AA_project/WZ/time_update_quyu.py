# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    automodated update wz quyu k3 depend on area js file and time

user:
    python time_update_quyu.py
------------------------------------------------
"""
import json
import os
import random
import sys
import time

import arcpy

reload(sys)
sys.setdefaultencoding('utf-8')

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/15"

TIME_FOMMATTER = '%Y-%m-%d-%H-%M'

area_folder = r'C:\tomcat\webapps\tsnav\live'
time_conf = r'C:\tomcat\webapps\tsnav\live\lastupdatetime.js'
quyu_shape = r'C:\arcgisserver\directories\arcgissystem\arcgisinput\wz3\wz_qy2.MapServer\extracted\cd\wz_py\WZ_QY.shp'
quyu_fields = ['netid', 'k3']


def main():
    print 'start'
    with open(time_conf, 'r') as ft:
        datas = json.load(ft)
        caltime = datas['date']

    area_file = 'area' + caltime + '.js'
    area = os.path.join(area_folder, area_file)

    with open(area, 'r') as f:
        datas = json.load(f)
        qy_210 = datas['a_210']
        qy_211 = datas['a_211']
        qy_212 = datas['a_212']
        qy_213 = datas['a_213']

    with arcpy.da.UpdateCursor(quyu_shape, quyu_fields) as cursor:
        for row in cursor:
            if row[0] == 210:
                row[1] = qy_210
                cursor.updateRow(row)
            elif row[0] == 211:
                row[1] = qy_211
                cursor.updateRow(row)
            elif row[0] == 212:
                row[1] = qy_212
                cursor.updateRow(row)
            elif row[0] == 213:
                row[1] = qy_213
                cursor.updateRow(row)
            else:
                pass

    print 'end'


if __name__ == '__main__':
    randnum = random.randrange(20, 35)
    sec = randnum / 10
    time.sleep(sec)
    main()
