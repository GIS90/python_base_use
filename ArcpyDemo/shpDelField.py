import os
import arcpy
import math

'''

for j in range(100,200,12):
    print j




'''
print "start"


#����·��
inputspace=r"D:\test\05 ����ʡ\����ʡ"



arcpy.env.workspace=inputspace

x=0

for i in arcpy.ListFiles('*.shp'):
   
    arcpy.DeleteField_management(i,"Join_Count")
    arcpy.DeleteField_management(i,"TARGET_FID")
    arcpy.DeleteField_management(i,"Id")#Id     Id_1      Join_Count    TARGET_FID

    print"ִ�д���X=",x,"        ","ִ��ͼ��Ϊ",i
    x=x+1
        




print "��������ִ��",x-1,"��"
print"finish all"


print "---------^ _ ^------------����˧-----------^ _ ^----------"
