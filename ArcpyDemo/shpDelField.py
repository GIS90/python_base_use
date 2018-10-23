import os
import arcpy
import math

'''

for j in range(100,200,12):
    print j




'''
print "start"


#输入路径
inputspace=r"D:\test\05 江苏省\江苏省"



arcpy.env.workspace=inputspace

x=0

for i in arcpy.ListFiles('*.shp'):
   
    arcpy.DeleteField_management(i,"Join_Count")
    arcpy.DeleteField_management(i,"TARGET_FID")
    arcpy.DeleteField_management(i,"Id")#Id     Id_1      Join_Count    TARGET_FID

    print"执行次数X=",x,"        ","执行图层为",i
    x=x+1
        




print "整个程序共执行",x-1,"次"
print"finish all"


print "---------^ _ ^------------你真帅-----------^ _ ^----------"
