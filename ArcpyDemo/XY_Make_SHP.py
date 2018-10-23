# - * - coding: utf-8 - * -


"""
此工具用于文本数据转为要素数据，主要用到MakeXYEventLayer_management函数
SaveToLayerFile_management函数
CopyFeatures_management函数
编程思想：
      1.获取源数据text格式
      2.利用MakeXYEventLayer_management进行数据格式转换,生成临时文件
      3.将临时文件转换的数据保存为.lay图层
      4.最后把Layer图层数据转为Shpfile数据

备注：
      1.此工具本人只测试text已经成功，别的格式也许需要调试。
      2.出现问题，本人概不负责
      3.如有雷同，纯属抄袭
      4.此工具为OS GIS Python Tool
      5.联系方式：QQ:GISじ★土匪♂→LBS亮，gaoming971366@163.com
"""

import datetime
import os
import arcpy

starttime = datetime.datetime.now()
print "Python Tool Start,Time Is:", starttime
for i in range(1, 3):
    print ""

# 工作空间,设置text,excel等数据放置的位置
workspace = r"E:\test"

print "Paramter Seted Up And Executing,Please Waite For It.................."

# 遍历的后缀可以是.dbf,.txt,xls,csv等等
arcpy.env.workspace = workspace
try:
    for txt in arcpy.ListFiles("*.txt"):
        # MakeXYEventLayer_management的参数设置、
        # X值
        in_x_field = "Field5"
        # Y值
        in_y_field = "Field6"
        # 输出的图层名称
        out_layer = txt
        # 输出数据的空间参考,可选参数
        spatial_reference = ""
        # 数据的Z值，也就是高程值，可选参数
        in_z_field = ""

        print "Paramter Seting Up,Inspect Infromation Is:"
        print "workspace:", workspace
        print "in_x_field:", in_x_field
        print "in_y_field:", in_y_field
        print "out_layer:", out_layer
        print "spatial_reference:", spatial_reference
        print "in_z_field:", in_z_field

        # 实现txt转换为临时数据
        arcpy.MakeXYEventLayer_management(txt,
                                          in_x_field,
                                          in_y_field,
                                          out_layer)
        # 打印临时图层数据的个数
        data_num = arcpy.GetCount_management(out_layer)
        print "Layer Data Number Is:", data_num
        # 将临时数据转换为Layer图层数据,设置参数
        in_lay = out_layer
        out_lay = os.path.splitext(txt)[0] + '.lyr'
        # 路径设置ABSOLUTE&RELATIVE
        is_relative_path = "ABSOLUTE"
        # 8.3,9.0,9.1,9.2,9.3,10,10.1,默认值CURRENT
        version = "CURRENT"
        arcpy.SaveToLayerFile_management(in_lay,
                                         out_lay,
                                         is_relative_path,
                                         version)
        # 设置CopyFeatures_management参数，生成成果Shpfile数据

        in_Feature = out_lay
        # 如果输出要素类已存在并且覆盖选项设置为 true，则将首先删除输出
        # 如果输出要素类已存在并且覆盖选项设置为 false，则操作将失败
        out_feature_class = os.path.splitext(txt)[0] + '.shp'
        # 输出为 ArcSDE 地理数据库或文件地理数据库时应用的地理数据库配置关键字，String类型
        config_keyword = ""
        # 参数仅适用于文件地理数据库和ArcSDE地理数据库要素类,Double类型
        spatial_grid_1 = ""
        spatial_grid_2 = ""
        spatial_grid_3 = ""
        arcpy.CopyFeatures_management(in_Feature,
                                      out_feature_class)

        print txt, "Generated Is Success....................................."






except Exception as e:
    print "It Occur Error,Information Is:", str(e)

for i in range(1, 3):
    print ""
endtime = datetime.datetime.now()
print "Python Tool End,Time Spend Is:", (endtime - starttime)
