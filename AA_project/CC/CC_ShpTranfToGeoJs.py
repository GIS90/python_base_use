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


def ShpGeoJsonToJson(shpField, shpPath):
    """
    将shp类型数据转为Json数据
    :param shpField: shp数据进行写入Json的标识字段
    :param shpPath: 存放shp数据的文件夹路径
    :return:执行错误，退出脚本
    """
    assert isinstance(shpPath, basestring)
    assert isinstance(shpField, list)
    arcpy.env.workspace = shpPath
    try:
        for shp in arcpy.ListFiles("*.shp"):
            shpData = os.path.join(shpPath, shp)
            jsonFile = os.path.join(shpPath, (os.path.splitext(shp)[0] + '_esri.js'))
            if os.path.exists(jsonFile):
                print '%s File Is Exists , Delete' % jsonFile
                os.unlink(jsonFile)
            f_w = codecs.open(jsonFile, 'w', 'utf-8')
            f_w.write('{')
            f_w.write('"displayFieldName": "NAME_CHN",')
            f_w.write(' "fieldAliases": {"%s": "%s"},' % (shpField[0], shpField[0]))
            f_w.write('"geometryType": "esriGeometryPolyline",')
            f_w.write('"spatialReference": {"wkid": 4326,"latestWkid": 4326},')
            f_w.write('"fields": [{"name": "%s","type": "esriFieldTypeOID","alias": "%s"}],'
                      % (shpField[0], shpField[0]))
            f_w.write('"features": [')
            rowNum = GetShpRowNums(shpData)
            n = 1
            with arcpy.da.SearchCursor(shpData, shpField) as cursor:
                for row in cursor:

                    objectid = int(row[0])
                    geo = str(row[1]).split(':')[1].split(',"')[0]
                    geo_spl = geo.split('[[[')[1].split(']]]')[0].split('],[')
                    geo_new = '[[['
                    for i in range(0, len(geo_spl)):
                        i_new = geo_spl[i].split(',')
                        for ii in range(0, len(i_new)):
                            value = str(float(i_new[ii]))
                            geo_new += value
                            if ii == 0:
                                geo_new += ','
                        if i < len(geo_spl) - 1:
                            geo_new += '],['
                    geo_new += ']]]'
                    f_w.write('{')
                    f_w.write('"attributes": {"%s": %d},' % (shpField[0], objectid))
                    f_w.write('"geometry": {"paths":%s}' % geo_new)
                    if n != rowNum:
                        f_w.write('},')
                        n += 1
                    else:
                        f_w.write('}]}')
            print '%s Is Transfer To Json Success ！' % str(jsonFile)
            f_w.close()
    except Exception as e:
        print 'Occur Exception : %s' % e.message
        print 'Tools Is Execute Failure !'
        sys.exit(0)


# 主函数入口
if __name__ == '__main__':
    print '*************************************************'
    print 'Ihe Python Tool Start Working !'
    startTime = datetime.datetime.now()
    print '*****Start Time : %s*****' % startTime
    path = r'E:\data\cc_js'
    fields = ["OBJECTID", "SHAPE@JSON"]
    if not os.path.exists(path):
        print 'Path is not exist .'
        sys.exit(0)
    ShpGeoJsonToJson(fields, path)
    print 'Tools Is Execute Success !'
    endTime = datetime.datetime.now()
    costTime = (endTime - startTime).seconds
    print '*****Cost Time : %s s.*****' % costTime
    print '*************************************************'
