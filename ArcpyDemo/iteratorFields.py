# -*-coding:utf-8-*-






import arcpy

inputSpace = r'E:\data\ty\clip'
arcpy.env.workspace = inputSpace

for shp in arcpy.ListFiles('*.shp'):
    print shp
    fields = arcpy.ListFields(shp)
    print fields
    for field in fields:
        print ("{0} is a type of {1} with a length of {2}" .format(field.name, field.type, field.length))



    cursor = arcpy.SearchCursor(shp)
    print shp

    for row in cursor:
        for field in fields:
            print "%-10s %s %-10s %s %s" % (field.name, ":", field.type, "----------", row.getValue(field.name))
