# - * - coding: utf-8 - * -


"""
此工具用于文本数据转为要素数据，主要用到MakeXYEventLayer_management函数
编程思想：
      1.获取源数据text格式
      2.利用MakeXYEventLayer_management进行数据格式转换,生成临时文件
      3.将临时文件转换的数据保存为.lay图层
      4.最后把Layer图层数据转为shpFile数据
"""

import os
import arcpy
import datetime
import shutil


def makePoint(dSour, dType, dFields):

    for i in range(1, 2):
        print ""
    print "Paramter Seted Up And Executing,Please Waite For It.................."
    # 工作空间
    arcpy.env.workspace = dSour

    for d in arcpy.ListFiles(dType):
        fileSour = os.path.join(dSour, os.path.splitext(d)[0])
        fileDestLayer = fileSour + '\\' + 'Layer'
        fileDestPoint = fileSour + '\\' + 'Point'
        isExtistSour = os.path.exists(fileDestLayer)
        if not isExtistSour:
            os.makedirs(fileSour)
        else:
            shutil.rmtree(fileSour)
            os.makedirs(fileSour)
        isExtistLayer = os.path.exists(fileDestLayer)
        if not isExtistLayer:
            os.makedirs(fileDestLayer)
        else:
            shutil.rmtree(fileDestLayer)
            os.makedirs(fileDestLayer)
        isExtistLayer = os.path.exists(fileDestLayer)
        if not isExtistLayer:
            os.mkdir(fileDestLayer)
        else:
            shutil.rmtree(fileDestLayer)
            os.mkdir(fileDestLayer)
        isExtistPoint = os.path.exists(fileDestPoint)
        if not isExtistPoint:
            os.mkdir(fileDestPoint)
        else:
            shutil.rmtree(fileDestPoint)
            os.mkdir(fileDestPoint)
        # MakeXYEventLayer_management的参数设置
        # X值
        in_x_field = dFields[0]
        # Y值
        in_y_field = dFields[1]
        # 输出的图层名称
        out_layer = d
        # 输出数据的空间参考,可选参数
        spatial_reference = ""
        # 数据的Z值，也就是高程值，可选参数
        in_z_field = ""

        print "Paramter Seting Up,Inspect Infromation Is:"
        print "workspace:", dSour
        print "in_x_field:", in_x_field
        print "in_y_field:", in_y_field
        print "out_layer:", out_layer
        print "spatial_reference:", spatial_reference
        print "in_z_field:", in_z_field
        try:
            # 实现txt转换为临时数据
            arcpy.MakeXYEventLayer_management(d,
                                              in_x_field,
                                              in_y_field,
                                              out_layer)
            # 打印临时数据的个数
            data_num = arcpy.GetCount_management(out_layer)
            print "Layer Data Number Is:", data_num
        except Exception as me:
            print 'MakeLayer.MakeXYEventLayer_management() occur exceprion : %s' % me.message

        # 将临时数据转换为Layer图层数据,设置参数
        in_lay = out_layer
        out_layName = os.path.splitext(d)[0] + '.lyr'
        out_lay = os.path.join(fileDestLayer, out_layName)
        # 路径设置ABSOLUTE&RELATIVE
        is_relative_path = "ABSOLUTE"
        # 8.3,9.0,9.1,9.2,9.3,10,10.1,默认值CURRENT
        version = "CURRENT"
        # arcpy.env.workspace=fileDes
        try:
            arcpy.SaveToLayerFile_management(in_lay,
                                             out_lay,
                                             is_relative_path,
                                             version)
        except Exception as se:
            print 'MakeLayer.SaveToLayerFile_management() occur exceprion : %s' % se.message
        # 设置CopyFeatures_management参数，生成成果Shpfile数据
        in_Feature = out_lay
        # 如果输出要素类已存在并且覆盖选项设置为 true，则将首先删除输出
        # 如果输出要素类已存在并且覆盖选项设置为 false，则操作将失败
        out_feature_className = os.path.splitext(d)[0] + '.shp'
        out_feature_class = os.path.join(fileDestPoint, out_feature_className)
        # 输出为 ArcSDE 地理数据库或文件地理数据库时应用的地理数据库配置关键字，String类型
        config_keyword = ""
        # 参数仅适用于文件地理数据库和ArcSDE地理数据库要素类,Double类型
        spatial_grid_1 = ""
        spatial_grid_2 = ""
        spatial_grid_3 = ""
        try:
            arcpy.CopyFeatures_management(in_Feature,
                                          out_feature_class)
        except Exception as ce:
            print 'MakeLayer.SaveToLayerFile_management() occur exceprion : %s' % ce.message

        print "%s generated shpFile success------------------------------" % d


if __name__ == '__main__':

    dataSour = r"E:\data\XY"
    # 遍历的后缀可以是.dbf,.txt,xls,csv等等
    dataType = '*.csv'
    xyFields = ['dropoff_longitude', 'dropoff_latitude']
    starttime = datetime.datetime.now()
    print "Python Tool Start,Time Is : ", starttime
    # 调用def
    makePoint(dataSour, dataType, xyFields)

    endtime = datetime.datetime.now()
    print "Python Tool End,Time Spend Is:", (endtime - starttime)
