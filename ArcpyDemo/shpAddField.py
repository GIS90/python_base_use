#coding:utf-8


import os
import arcpy


print "start"
inputspace=r'E:\2015Project\ceshi.gdb'
arcpy.env.workspace=inputspace

x=0

for i in arcpy.ListFeatureClasses():

    arcpy.AddField_management(i,"PORT","text",50)
    arcpy.AddField_management(i,"NAME","text",50)
        
    print"finish part add"
    k=os.path.splitext(i)[0]
    print k

    x=x+1
       
