#-*- coding:utf-8 -*-


import pyodbc
import arcpy

# connDriver='{SQL Server}'
# connServer='localhost'
# connDB='QD_ProjectDB'
# connUID='sa'
# connPWD='123456'
#
# conn=pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
#                      %(connDriver,connServer,connDB,connUID,connPWD)))
#   %(connDri
# print conn
filePath=r'E:\2015Project\connectionToSDE.sde\sde.dbo.cs'

cursor=arcpy.UpdateCursor(filePath)
v=100
for row in cursor:
    row.setValue('value',v)
    v=v+10
    cursor.updateRow(row)
print 1