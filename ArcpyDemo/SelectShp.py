# -*- coding: utf-8 -*-

import arcpy

def fields(shp):
    field_names = [f.name for f in arcpy.ListFields(shp)]
    print field_names

def select():
    pass




if __name__ == '__main__':
    sqlShp = r'E:\data\bjpoi\bjqx.shp'
    selShp = r'E:\data\bjpoi\bjpoi.shp'
    fields(sqlShp)

