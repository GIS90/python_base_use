# coding=utf8
# !/usr/bin/python

from Core.ShpTranfToGeoJs import *



objectid = range(1, 100, 1)
path = r'D:\Py_file\WebSocketServer\Data'
fields = ["OBJECTID", "SHAPE@JSON"]
print ShpGeoJsonToJson(objectid, path, fields)

