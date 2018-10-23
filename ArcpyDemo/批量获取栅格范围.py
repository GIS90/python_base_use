# -*- coding: utf-8 -*-


import os

import arcpy

print "Python Tool Start--------^_^---------"

InputSpace = r"E:"
OutputSpace = r"E:\test"

OutputName = os.path.split(InputSpace)[1]

num = 0
arcpy.env.workspace = InputSpace

try:

    rasterList = arcpy.ListRasters("*", "IMG")

    if rasterList:
        for raster in rasterList:
            OutputName = os.path.splitext(raster)[0]
            OutputName1 = OutputName + ".shp"
            outGeom = "POLYGON"

            print "执行次数num=", num, "被执行要素：", raster, "生成要素：", OutputName1

            arcpy.RasterDomain_3d(raster, os.path.join(OutputSpace, OutputName1), outGeom)
            print "Finish."
    else:
        "There are no IMG files in the " + arcpy.env.workspace + " directory."

except Exception as e:
    print e.message

print "sum=", num, "All Finish"
