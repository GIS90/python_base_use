# coding:utf-8

import arcpy
import os
import sys
import codecs
import datetime

"""
    用来把shp数据(polygen类型)转为相对应的ESRI Service Json格式数据
"""


def Count(shape):
    """
    获取shp数据包含的数量
    :param shape: shp数据的文件
    :return: 返回shp数据的包含的数据个数
    """
    num = 0
    with arcpy.da.SearchCursor(shape, ["SHAPE@"]) as cursor:
        for row in cursor:
            num += 1
    print '%s num is %d' % (shape, num)
    return num


def transfer(path, fields):
    """
    将shp类型数据转为Json数据
    :param fields: shp数据进行写入Json的标识字段
    :param path: 存放shp数据的文件夹路径
    :return:执行错误，退出脚本
    """
    assert isinstance(path, basestring)
    assert isinstance(fields, list)
    
    arcpy.env.workspace = path

    for shp in arcpy.ListFiles("*.shp"):
        shape = os.path.join(path, shp)
        jsfile = os.path.join(path, (os.path.splitext(shp)[0] + '_esri.js'))
        if os.path.exists(jsfile):
            print "%s is exist,delete it." % str(os.path.split(jsfile)[1])
            os.unlink(jsfile)
            
        fw = codecs.open(jsfile, 'w', 'utf-8')
        fw.write('{')
        fw.write('"displayFieldName": "NAME",')
        fw.write(' "fieldAliases": {"%s": "%s"},' % (fields[0], fields[0]))
        fw.write('"geometryType": "esriGeometryPolygon",')
        fw.write('"spatialReference": {"wkid": 4326,"latestWkid": 4326},')
        fw.write('"fields": [{"name": "%s","type": "esriFieldTypeOID","alias": "%s"}],'
                  % (fields[0], fields[0]))
        fw.write('"features": [')
        count = Count(shape)
        n = 1
        with arcpy.da.SearchCursor(shape, fields) as cursor:
            for row in cursor:
                name = row[0]
                print name
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
                fw.write('{')
                fw.write('"attributes": {"%s": %s},' % (fields[0], name))
                fw.write('"geometry": {"rings":%s}' % geo_new)
                if n != count:
                    fw.write('},')
                    n += 1
                else:
                    fw.write('}]}')

            print '%s is tranfter success ！' % str(jsfile)
            fw.close()



# 主函数入口
if __name__ == '__main__':
    
    shpdir = r'E:\data\ty\country'
    fields = ["netid", "SHAPE@JSON"]
    
    startime = datetime.datetime.now()
    print '*****start time : %s*****' % startime
    
    if not os.path.exists(shpdir):
        print '%s is not exist, please input availiable path.' % shpdir
        sys.exit(0)
    
    if transfer(shpdir, fields):
        print 'tools is execute success !'
    else:
        print 'exception exit'
        sys.exit(0)
        
    endtime = datetime.datetime.now()
    costime = (endtime - startime).seconds
    print '*****cost time : %s s.*****' % costime
