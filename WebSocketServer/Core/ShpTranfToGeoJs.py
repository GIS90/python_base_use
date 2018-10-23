# coding:utf-8

import arcpy
import os


"""
    用来把shp数据(polline类型)转为相对应的ESRI Service Json格式数据
"""


def ShpGeoJsonToJson(shpId, shpPath, shpFields):
    """
    将shp类型数据转为Json数据
    :param shpId: shp数据进行写入Json的标识字段
    :param shpFields: shp数据进行写入Json的标识字段
    :param shpPath: 存放shp数据的文件夹路径
    :return:执行错误，退出脚本
    """
    assert isinstance(shpPath, basestring)
    assert isinstance(shpFields, list)
    assert isinstance(shpId, list)

    arcpy.env.workspace = shpPath
    data = ''
    shpData = os.path.join(shpPath, 'linkgeo.shp')
    print shpData
    data += '{'
    data += '"displayFieldName": "NAME_CHN",'
    data += ' "fieldAliases": {"%s": "%s"},' % (shpFields[0], shpFields[0])
    data += '"geometryType": "esriGeometryPolyline",'
    data += '"spatialReference": {"wkid": 4326,"latestWkid": 4326},'
    data += '"fields": [{"name": "%s","type": "esriFieldTypeOID","alias": "%s"}],' % (shpFields[0], shpFields[0])
    data += '"features": ['
    rowNum = len(shpId)
    n = 1
    with arcpy.da.SearchCursor(shpData, shpFields) as cursor:
        for row in cursor:
            objectid = int(row[0])
            for sid in shpId:
                if int(sid) == objectid:
                    geo = str(row[1]).split(':')[1].split(',"')[0]
                    data += '{'
                    data += '"attributes": {"%s": %d},' % (shpFields[0], objectid)
                    data += '"geometry": {"paths":%s}' % geo
                    if n != rowNum:
                        data += '},'
                        n += 1
                    else:
                        data += '}]}'
    return data



