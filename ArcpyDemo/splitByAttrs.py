#coding:gbk



import arcpy
import os




#�ļ���·��
filePath=r'E:\connectToSDE'
arcpy.env.workspace=filePath
for shp in arcpy.ListFiles('*.shp'):
    shpSour=os.path.join(filePath,shp)
    #Ҫ�ֱ���ȡ����������
    field='name'
    cursor=arcpy.SearchCursor(shpSour)
    try:
        for row in cursor:
            name=row.getValue(field)
            shpDest=os.path.join(filePath,(name+'.shp'))
            sql="\"name\" = '%s'"%name
            arcpy.Select_analysis(shpSour,shpDest,sql)
            print '%s Extract Success !'%name
    except Exception as e:
        print e.message




