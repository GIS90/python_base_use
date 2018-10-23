#coding:utf-8


import zipfile
import os
import arcpy

filePath=r'D:\Temp'
zipContentpath=filePath
arcpy.env.workspace=filePath
for zfile in arcpy.ListFiles('*.zip'):
    zPath=os.path.join(filePath,zfile)
    print '%s Content Is :'%zPath
    z=zipfile.ZipFile(zPath,'r')
    for zfContentName in z.namelist():
        z.extract(zfContentName,zipContentpath)
        print '%s zip Success !'%zfContentName

