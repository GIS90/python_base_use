
# -*- coding: utf-8 -*-

#导入包

import arcpy
import os
import sys




print "Python Tool Start--------^_^---------"


#裁剪文件的工作空间
InputSpace=r"F:\data\fuzhou_data"
#结果文件的存放目录
OutputSpace=r"F:\data\shp"
#被裁剪文件路径+名称
ClipShpfile=r"F:\data\fuzhou_map_Demo"

ClipName=os.path.split(ClipShpfile)[1]

#实现的主体
num=0
arcpy.env.workspace=InputSpace

for i in arcpy.ListFiles("*.shp"):
    num=num+1
    print r"执行次数num=",num,r"被裁剪要素：",i,r"裁剪要素：",ClipName
    try:
        arcpy.Clip_analysis(os.path.join(InputSpace, i),ClipShpfile, os.path.join(OutputSpace,i), '.0000001 DecimalDegrees')
        print "Finish"
    except Exception as e:
        print(e.message)




print "sum=",num,"All Finish"
