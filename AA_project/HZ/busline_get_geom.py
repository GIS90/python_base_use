# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: busline_get_geom.py
@time: 2016/8/31 18:37
@describe: 
@remark: 
------------------------------------------------
"""

import os
import codecs
import arcpy


shape_field_lid = ("LinkIdBus", "lineDirect")
shape_field_xy = ("SHAPE@X", "SHAPE@Y")
shape_dir = r"E:\data\hz_bus\busline_ne0"
arcpy.env.workspace = shape_dir


def get_shape_num(shp, query):
    """
    获取shp数据包含的数量
    :param shp: shp数据的文件路径
    :return: 返回shp数据的包含的数据个数
    """
    num = 0
    with arcpy.da.SearchCursor(shp, ["SHAPE@"], query) as cursor:
        for row in cursor:
            num += 1
    print '%s num is %d' % (query, num)
    return num

for shp in arcpy.ListFiles('*.shp'):
    line_lids = []
    shape = os.path.join(shape_dir, shp)
    desc = arcpy.Describe(shape)
    js_file = os.path.abspath(os.path.join(shape_dir, (os.path.splitext(shp)[0] + ".js")))
    if os.path.exists(js_file):
        os.unlink(js_file)
    if str(desc.shapeType).lower() == "point":
        print "---------------" + js_file + "---------------"
        f_w = codecs.open(js_file, 'w', 'utf-8')
        f_w.write("{")
        with arcpy.da.SearchCursor(shape, shape_field_lid) as lid_cursor:
            for row in lid_cursor:
                link_id_bus = str(int(row[0]))
                line_direct = str(int(row[1]))
                lid = link_id_bus + "_" + line_direct
                if lid not in line_lids:
                    line_lids.append(lid)
        line_num = 1
        line_nums = len(line_lids)
        for line_lid in line_lids:
            print line_lid
            line_geoms = ""
            link_id_bus = line_lid.split("_")[0]
            line_direct = line_lid.split("_")[1]
            where_clause = """LinkIdBus = %d and lineDirect = %s""" % (int(link_id_bus), int(line_direct))
            row_nums = get_shape_num(shape, where_clause)
            row_num = 1
            with arcpy.da.SearchCursor(shape, shape_field_xy, where_clause) as xy_cursor:
                line_geoms += "[["
                for row in xy_cursor:
                    x = str(float(row[0]))
                    y = str(float(row[1]))
                    line_geoms += "[" + x + "," + y + "]"
                    if row_num < row_nums:
                        line_geoms += ","
                        row_num += 1
                line_geoms += "]]"
            line = '"%s": %s' % (line_lid, line_geoms)
            f_w.write(line)
            if line_num < line_nums:
                f_w.write(",")
                line_num += 1
            else:
                f_w.write("}")
        f_w.close()
        print "success."




