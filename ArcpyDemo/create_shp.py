import arcpy, os



print "start"

arcpy.env.workspace="E:/test"
outLocation ="E:/test"



arcpy.CreateFeatureclass_management(outLocation, "≤‚ ‘.shp", "POLYGON")




#if arcpy.Exists("≤‚ ‘.shp"):
#    arcpy.Delete_management("≤‚ ‘.shp")




print "finish"
