# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: edit_arcpy_test.py
@time: 2016/11/14 14:00
@describe: 
@remark: 
------------------------------------------------
"""

import arcpy

fc = 'C:/Portland/Portland.gdb/Land/Parks'
workspace = 'C:/Portland/Portland.gdb'
layer_name = 'Parks'

try:
    arcpy.MakeFeatureLayer_management(fc, layer_name)
    arcpy.SelectLayerByAttribute_management(
        layer_name, 'NEW_SELECTION',
        """CUSTODIAN = 'City of Portland'""")
    with arcpy.da.Editor(workspace) as edit:
        arcpy.CalculateField_management(
            layer_name, 'Usage', '"PUBLIC"', 'PYTHON')

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

