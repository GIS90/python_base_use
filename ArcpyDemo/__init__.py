__author__ = 'Administrator'




# fc = r'C:\Users\tang\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\Connection to ..sde\gis.DBO.aaaaaaaaaa'
# fc = r'C:\Users\tang\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\work.sde\work.DBO.GIS_WEAK_GRID20160722allcity'
# fields = ['x', 'y', 'SHAPE@']
# arcpy.env.workspace = r'C:\Users\tang\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\work.sde'
# edit = arcpy.da.Editor(arcpy.env.workspace)
# edit.startEditing(False, True)
# edit.startOperation()
# with arcpy.da.UpdateCursor(fc, fields) as cursor:
#     for row in cursor:
#         row[0] = row[2].firstPoint.X
#         row[1] = row[2].firstPoint.Y
#         print row[0], row[1], row[2]
#         cursor.updateRow(row)
#
# edit.end
