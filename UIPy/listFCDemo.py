

import os
import arcpy

f=r'F:\ConnectionToSQL.sde'
arcpy.env.workspace=f
for i in arcpy.ListFeatureClasses(feature_type='Polygon'):
    print i