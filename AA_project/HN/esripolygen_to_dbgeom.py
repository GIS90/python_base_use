# coding:utf-8
"""
    用来把shp数据(polygon类型)转为相对应的EChart后台的Json格式数据
"""
import codecs
import datetime
import os
import sys

import arcpy

from decimal import Decimal


TIME_FORMMATER = '%y-%m-%d %H:%M:%S'


def getshapnums(shape):
    """
    获取shp数据包含的数量
    :param shape: shp数据的文件路径
    :return: 返回shp数据的包含的数据个数
    """
    num = 0
    with arcpy.da.SearchCursor(shape, ["SHAPE@"]) as cursor:
        for row in cursor:
            num += 1
    print '%s num is %d' % (shape, num)
    return num


def transfer(shpfields, shppath, precision):
    """
    将shp类型数据转为Json数据
    :param shpfields: shp数据进行写入Json的标识字段
    :param shppath: 存放shp数据的文件夹路径
    :param precision: shape的坐标信息的精度
    :return:
    """
    assert isinstance(shppath, basestring)
    assert isinstance(shpfields, list)
    assert isinstance(precision, int)

    arcpy.env.workspace = shppath
    for shp in arcpy.ListFiles("*.shp"):
        shape = os.path.join(shppath, shp)
        shpfile = os.path.join(shppath, (os.path.splitext(shp)[0] + '.txt'))
        if os.path.exists(shpfile):
            print '%s file is exists , deleting' % shpfile
            os.unlink(shpfile)
        fw = codecs.open(shpfile, 'w', 'utf-8')
        fw.write("typeid;name;lon;lat;area;geom\n")
        fcprec = "0."
        for i in range(precision):
            fcprec += "0"
        num = 0
        shpnum = getshapnums(shape)
        try:
            with arcpy.da.SearchCursor(shape, shpfields) as cursor:
                for row in cursor:
                    num += 1
                    if isinstance(row[0], unicode):
                        name = row[0].encode('utf-8')
                    else:
                        name = str(row[0]).decode('utf-8')
                    fcname = row[0]
                    infos = row[1]
                    fcgeom = str(infos).split(':[[[')[1].split(']]],"')[0]
                    geo_s_1 = fcgeom.split(']],[[')
                    fcgeom_new = '[[['
                    for g in range(0, len(geo_s_1)):
                        geo_s_2 = geo_s_1[g].split('],[')
                        for i in range(0, len(geo_s_2)):
                            i_new = geo_s_2[i].split(',')
                            for ii in range(0, len(i_new)):
                                value = str(Decimal(i_new[ii]).quantize(Decimal(fcprec)))
                                fcgeom_new += value
                                if ii == 0:
                                    fcgeom_new += ','
                            if i < len(geo_s_2) - 1:
                                fcgeom_new += '],['
                        if g < len(geo_s_1) - 1:
                            fcgeom_new += '],['
                    fcgeom_new += ']]]'

                    fcentpoint = tuple(row[2])
                    fclon = Decimal(fcentpoint[0]).quantize(Decimal(fcprec))
                    fclat = Decimal(fcentpoint[1]).quantize(Decimal(fcprec))
                    fcarea = float(row[3]) * 1000 * 1000 * 10000
                    line = "1;%s;%f;%f;%d;%s" % (fcname, fclon, fclat, fcarea, fcgeom_new)
                    fw.write(line)
                    fw.write('\n')
                fw.close()
                print '%s is transfer to json success ！' % str(shpfile)
        except Exception as e:
            print 'Occur exception : %s' % e.message
            sys.exit(1)


def main():

    print 'the python tool start working !'
    startime = datetime.datetime.now()
    print 'start time : %s' % startime.strftime(TIME_FORMMATER)
    path = r'E:\data\hn'
    fields = ["NAME", "SHAPE@JSON", "SHAPE@XY", "SHAPE@AREA"]
    precision = 6
    if not os.path.exists(path) or not os.path.isdir(path):
        print 'path is not exist or not folder.'
        sys.exit(0)
    else:
        transfer(fields, path, precision)
    print 'Tools is execute success !'
    endtime = datetime.datetime.now()
    costime = (endtime - startime).seconds
    print 'cost time : %s s' % costime


# 主函数入口
if __name__ == '__main__':
    main()



"""
UPDATE area_base,
hn_region
SET area_base.paths = hn_region.geom
WHERE
area_base.typeId = hn_region.typeid
AND area_base.`name` = hn_region.`name`
"""
