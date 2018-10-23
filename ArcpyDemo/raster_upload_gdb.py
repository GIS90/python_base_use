# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: raster_upload_gdb.py
@time: 2016/8/30 19:28
@describe: 
@remark: 
------------------------------------------------
"""
import arcpy
import os


def upload_gdb(jpg_dir, gdb_path):
    arcpy.env.workspace = jpg_dir
    rasters = arcpy.ListRasters("*", "jpg")
    for raster in rasters:
        raster_path = os.path.abspath(os.path.join(jpg_dir, raster))
        try:
            arcpy.RasterToGeodatabase_conversion(raster_path,
                                                 gdb_path,
                                                 "")
        except Exception as e:
            print "%s upload to %s failure: %s." % (raster, gdb_path, e.message)
        else:
            print "%s upload to %s success." % (raster, gdb_path)

    print "All raster upload over."


if __name__ == '__main__':

    jpg_dir = r"E:\data\jpg"
    gdb_path = r"E:\data\Rasters.gdb"
    upload_gdb(jpg_dir, gdb_path)
