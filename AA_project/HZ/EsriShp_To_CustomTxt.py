# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/11'
"""

# coding:utf-8

import arcpy
import os
import sys
import codecs
import datetime

"""
    用来把shp数据(polline类型)转为相对应的ESRI Service Json格式数据
"""


def GetShpRowNums(shpData):
    """
    获取shp数据包含的数量
    :param shpData: shp数据的文件路径
    :return: 返回shp数据的包含的数据个数
    """
    rowNums = 0
    with arcpy.da.SearchCursor(shpData, ["SHAPE@"]) as cursor:
        for row in cursor:
            rowNums += 1
    print '%s num is %d' % (shpData, rowNums)
    return rowNums


def ShpGeoJsonToTxt(shpField, shpPath):
    """
    将shp类型数据转为Json数据
    :param shpField: shp数据进行写入Json的标识字段
    :param shpPath: 存放shp数据的文件夹路径
    :return:执行错误，退出脚本
    """
    assert isinstance(shpPath, basestring)
    assert isinstance(shpField, list)
    arcpy.env.workspace = shpPath

    for shp in arcpy.ListFiles("*.shp"):
        try:
            shpData = os.path.join(shpPath, shp)
            txtFile = os.path.join(shpPath, (os.path.splitext(shp)[0] + '.txt'))
            if os.path.exists(txtFile):
                print '%s File Is Exists , Delete' % txtFile
                os.unlink(txtFile)
            f_w = codecs.open(txtFile, 'w', 'utf-8')
            f_w.write("FID LineId LineDirect SHAPE@JSON")
            f_w.write('\n')

            with arcpy.da.SearchCursor(shpData, shpField) as cursor:
                for row in cursor:
                    print row[0]
                    oId = int(row[0])
                    lineId = int(row[1])
                    lineDirect = int(row[2])
                    geo = str(row[3]).split(':[[[')[1].split(']]],"')[0]
                    geo_s_1 = geo.split(']],[[')

                    geo_new = '[[['
                    for g in range(0, len(geo_s_1)):
                        geo_s_2 = geo_s_1[g].split('],[')
                        for i in range(0, len(geo_s_2)):
                            i_new = geo_s_2[i].split(',')
                            for ii in range(0, len(i_new)):
                                value = str(float(i_new[ii]))
                                geo_new += value
                                if ii == 0:
                                    geo_new += ','
                            if i < len(geo_s_2) - 1:
                                geo_new += '],['
                        if g < len(geo_s_1) - 1:
                            geo_new += '],['
                    geo_new += ']]]'

                    line = str(oId) + ' ' + str(lineId) + ' ' + str(lineDirect) + ' ' + geo_new
                    f_w.write(line)
                    f_w.write('\n')
            print '%s Is Transfer To Json Success ！' % str(txtFile)
            f_w.close()
        except Exception as e:
            print 'Occur Exception : %s' % e.message
            print 'Tools Is Execute Failure !'
            sys.exit(0)


# 主函数入口
if __name__ == '__main__':

    print '*************************************************'
    fmt = '%Y-%m-%d %H:%M:%S'
    startTime = datetime.datetime.now()
    now = startTime.strftime(fmt)
    print '%s start working :' % now
    path = r'E:\data\busline\busline'
    fields = ["FID", "LineId", "LineDirect", "SHAPE@JSON"]
    if not os.path.exists(path):
        print 'Path is not exist , please offer a available path.'
        sys.exit(0)
    ShpGeoJsonToTxt(fields, path)
    print 'Tools Is Execute Success !'
    endTime = datetime.datetime.now()
    costTime = (endTime - startTime).seconds
    print '*****Cost Time : %s s.*****' % costTime
    print '*************************************************'
