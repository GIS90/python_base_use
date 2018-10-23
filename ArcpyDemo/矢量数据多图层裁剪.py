# -*- coding: utf-8 -*-

# 导入包
import datetime
import os
import arcpy

startTime = datetime.datetime.now()
print "Python Tool Start--------^_^---------"

# 裁剪文件的工作空间
InputSpace = r"E:\@Project\Map2013City"
# 结果文件的存放目录
OutputSpace = r"E:\data\hn\hn"
# 被裁剪文件路径+名称
clip_features = r"E:\data\jn\jining.shp"

# 实现的主体，添加个变量用于处理次数
num = 1
# 设置工作空间
arcpy.env.workspace = InputSpace
for in_features in arcpy.ListFiles("*.shp"):
    clipName = os.path.splitext(in_features)[0]
    out_features = os.path.join(OutputSpace, clipName)
    cluster_tolerance = "0.0000001 DecimalDegrees"
    print "Execute num=", num, "Chip Feature is:", clipName
    try:
        arcpy.Clip_analysis(in_features,
                            clip_features,
                            out_features,
                            cluster_tolerance)
        print "Finish"
        num += 1
    except Exception as e:
        print e.message
endTime = datetime.datetime.now()
exeTime = (endTime - startTime).seconds
print "sum=", num - 1, "All Finish,Cost Time is :", exeTime, "s"
