# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# SHP文件的批量裁切，裁切框可以为多个文件，被裁切文件可以为多个，裁切后的结果分别存放在以裁切文件命名的文件夹中
# Created on: 2012-07-21 17:37:17.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------
import os
import shutil

import arcpy

# import wxPython

print 'a\ta'

sourceDir = r"E:\@Project\Map2013City"  # 被裁切文件存放的文件夹

targetDir = r"E:\data\ty\data"  # 裁切后结果文件存放的文件，子文件已裁切框的名称命名
cutDir = r"E:\data\ty\clip"  # 裁切框文件存放的文件夹


def do_Cut(sourceDir):
    i = 0  # 计数，裁切框数

    # 设置工作空间位置
    arcpy.env.workspace = cutDir
    print sourceDir
    # 遍历裁切框shp文件
    for cutFile in arcpy.ListFiles("*.shp"):
        i = i + 1
        # 依据裁切框名称新建文件夹
        okDir = os.path.join(targetDir, os.path.splitext(cutFile)[0])
        # 判断裁切后的结果文件夹是否存在，如果存在，则先删除，再新建；如果不存在，则直接新建
        if os.path.exists(okDir):
            shutil.rmtree(okDir)
            os.makedirs(okDir)
        else:
            os.makedirs(okDir)

        # 裁切框文件的完整路径
        cut1_shp = os.path.join(cutDir, cutFile)
        arcpy.env.workspace = sourceDir
        print sourceDir
        j = 0  # 计数，每个裁切框内的裁切文件数
        # 遍历被裁切的shp文件
        for file1 in arcpy.ListFiles("*.shp"):
            print file1
            j = j + 1
            # 裁切
            print u"裁切框", i, u"裁切文件", j, os.path.join(sourceDir, file1), cut1_shp, os.path.join(okDir, file1)
            arcpy.Clip_analysis(os.path.join(sourceDir, file1), cut1_shp, os.path.join(okDir, file1), ".0000001 DecimalDegrees")


if __name__ == '__main__':
    print 'start'
    do_Cut(sourceDir)
    print "all is ok"
