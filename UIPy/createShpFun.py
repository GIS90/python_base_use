


import arcpy
import sys




fileName=sys.argv[0]
workspace=sys.argv[1]
name=sys.argv[2]
shptype=sys.argv[3]
template=sys.argv[4]
has_m=sys.argv[5]
has_z=sys.argv[6]
gcs=sys.argv[7]
print fileName
print workspace


arcpy.env.workspace=workspace
arcpy.CreateFeatureclass_management(workspace,name,shptype)
print "Create "+name+" Success!"