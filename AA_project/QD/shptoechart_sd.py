# coding:utf-8

import codecs
import datetime
import os
import sys
from decimal import Decimal

import arcpy

"""
    用来把shp数据(polygon类型)转为相对应的EChart后台的Json格式数据
    山东省区域地图
"""


DRIVER = "ESRI Shapefile"
GDAL_FILE_CODE = "GDAL_FILENAME_IS_UTF8"
SHAPE_CODE = "SHAPE_ENCODING"


def get_row_count(shape):
    """
    获取shp数据包含的数量
    :param shape: shp数据
    :return: 返回shp数据的包含的数据个数
    """
    try:
        from osgeo import ogr
        from osgeo import gdal
    except ImportError as e:
        import ogr
        import gdal

    gdal.SetConfigOption(GDAL_FILE_CODE, "NO")
    gdal.SetConfigOption(SHAPE_CODE, "")
    ogr.RegisterAll()
    driver = ogr.GetDriverByName(DRIVER)
    ds = driver.Open(shape)
    # if ds is None:
    #     print "%s could not open" % shape
    #     reture 0
    # lyr = ds.GetLayerByIndex(0)
    # return lyr.GetFeatureCount(0)
    return 0 if ds is None else ds.GetLayerByIndex(0).GetFeatureCount(0)


def shp_to_ecjcson(shp_folder, shp_fields):
    """
    将shp类型数据转为Json数据
    :param shp_fields: shp数据进行写入Json的标识字段
    :param shp_folder: 存放shp数据的文件夹路径
    :return:
    """
    assert isinstance(shp_folder, basestring)
    assert isinstance(shp_fields, list)

    arcpy.env.workspace = shp_folder
    for shp_file in arcpy.ListFiles("*.shp"):
        shape = os.path.join(shp_folder, shp_file)
        shp_desc = arcpy.Describe(shape)
        if shp_desc.shapeType != "Polygon":
            print "%s is not polygon type" % shp_file
        ecjson = os.path.join(shp_folder, 'shandong.js')
        if os.path.exists(ecjson):
            print '%s file is exists , delete' % ecjson
            os.unlink(ecjson)
        shp_num = get_row_count(shape)
        print "feature count is %d" % shp_num
        f_w = codecs.open(ecjson, 'w', 'utf-8')
        f_w.write("{\n\t")
        f_w.write('"type": "FeatureCollection",\n\t')
        f_w.write('"cp":[118.7402,36.4307],\n\t')
        f_w.write('"size":"1500",\n\t')
        f_w.write('"features":[')
        num = 0
        with arcpy.da.SearchCursor(shape, shp_fields) as cursor:
            for row in cursor:
                f_w.write("\n\t\t")
                num += 1
                fc_id = int(row[0])
                fc_name = row[1]
                fc_childNum = int(row[2])
                fc_centos = list(row[3])
                # geomtry = str(row[4]).split(':[[[')[1].split(']]],"')[0]
                # geo_s_1 = geomtry.split(']],[[')
                # fc_geometry = '[[['
                # for g in range(0, len(geo_s_1)):
                #     geo_s_2 = geo_s_1[g].split('],[')
                #     for i in range(0, len(geo_s_2)):
                #         i_new = geo_s_2[i].split(',')
                #         for ii in range(0, len(i_new)):
                #             # value = str(Decimal.from_float(float(i_new[ii])).quantize(Decimal('0.0000')))
                #             value = str(float(i_new[ii]))
                #             fc_geometry += value
                #             if ii == 0:
                #                 fc_geometry += ','
                #         if i < len(geo_s_2) - 1:
                #             fc_geometry += '],['
                #     if g < len(geo_s_1) - 1:
                #         fc_geometry += '],['
                # fc_geometry += ']]]'
                fc_geometry = str(row[4]).split(':')[1].split(',"')[0].split('}')[0]
                line = '{"type": "Feature","properties":{"id":"%d","name":"%s","cp":%s,"childNum":%d},"geometry":{"type":"Polygon","coordinates":%s}}' \
                       % (fc_id, fc_name, fc_centos, fc_childNum, fc_geometry)
                f_w.write(line)
                if num < shp_num:
                    f_w.write(",")
                else:
                    f_w.write("\n\t]")
            f_w.write("\n}")
            f_w.close()
        print '%s Is Transfer To Json Success ！' % str(ecjson)


# 主函数入口
if __name__ == '__main__':
    print 'start....... !'
    start_time = datetime.datetime.now()
    print '*****Start time : %s*****' % start_time
    # shandong region
    shp_folder = r'E:\data\qd_data_js\shp'
    shp_fields = ["ID_2", "NL_NAME_2", "childNum", "SHAPE@XY", "SHAPE@JSON"]
    if not os.path.exists(shp_folder):
        print 'Path is not exist .'
        sys.exit(0)
    shp_to_ecjcson(shp_folder, shp_fields)
    print 'Tools ts execute success !'
    end_time = datetime.datetime.now()
    cost_time = (end_time - start_time).seconds
    print '*****Cost time : %s s.*****' % cost_time
    print '*************************************************'
