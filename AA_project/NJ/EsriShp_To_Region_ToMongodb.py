# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/11'
"""

# coding:utf-8

import arcpy
import os
import pymongo
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


"""
    用来把shp数据(polline类型)转为相对应的ESRI Service Json格式数据
"""


def ShpGeoJsonToMongdb(shpField, shpPath):
    """
    将shp类型数据转为Json数据
    :param shpField: shp数据进行写入Json的标识字段
    :param shpPath: 设置工作空间
    :return:执行错误，退出脚本
    """
    assert isinstance(shpPath, basestring)
    assert isinstance(shpField, list)
    arcpy.env.workspace = shpPath

    mgConn = pymongo.MongoClient(host='127.0.0.1', port=27017)
    mgDB = mgConn.sde
    mgCol = mgDB.path
    regList = []

    for shp in arcpy.ListFiles("*.shp"):
            shpData = os.path.join(shpPath, shp)
            with arcpy.da.SearchCursor(shpData, shpField) as cursor:
                for row in cursor:
                    regId = int(row[0])
                    regName = row[1]
                    geo = str(row[2]).split(':[[[')[1].split(']]],"')[0]
                    geo_s_1 = geo.split(']],[[')
                    regGeo = '[[['
                    for g in range(0, len(geo_s_1)):
                        geo_s_2 = geo_s_1[g].split('],[')
                        for i in range(0, len(geo_s_2)):
                            i_new = geo_s_2[i].split(',')
                            for ii in range(0, len(i_new)):
                                value = str(float(i_new[ii]))
                                regGeo += value
                                if ii == 0:
                                    regGeo += ','
                            if i < len(geo_s_2) - 1:
                                regGeo += '],['
                        if g < len(geo_s_1) - 1:
                            regGeo += '],['
                    regGeo += ']]]'
                    print regId
                    regDict = {}
                    regDict["regId"] = regId
                    regDict["regName"] = regName
                    regDict["regGeoPath"] = regGeo
                    # mgCol.insert_one(regDict)
                    regList.append(regDict)
            mgCol.insert_many(regList)

            print '%s is import to mongodb success ！' % shpData


# 主函数入口
if __name__ == '__main__':

    print '*************************************************'
    fmt = '%Y-%m-%d %H:%M:%S'
    startTime = datetime.datetime.now()
    now = startTime.strftime(fmt)
    print '%s start working :' % now
    path = r'E:\data\nj_js\zq_shp'
    fields = ["ID", "REGION", "SHAPE@JSON"]
    if not os.path.exists(path):
        print 'Path is not exist , please offer a available path.'
        sys.exit(0)
    ShpGeoJsonToMongdb(fields, path)
    print 'Tools Is Execute Success !'
    endTime = datetime.datetime.now()
    costTime = (endTime - startTime).seconds
    print '*****Cost Time : %s s.*****' % costTime
    print '*************************************************'
