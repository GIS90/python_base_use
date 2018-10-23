# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will update a layer's symbology with the symbology from
#          a layer file.  This script is intended to run as a script tool and
#          has four parameters:
#               1) Input Map Document,
#               2) Layer Name (auto populated using a validation script),
#               3) Layer File,
#               4) Output Map Document.

# Note: Geometry types, etc must match.  Read more about UpdateLayer in help.

import arcpy, os

#Read parameters from dialog
mxdPath = arcpy.GetParameterAsText(0)
dfName = arcpy.GetParameterAsText(1)
layerName = arcpy.GetParameterAsText(2)
layerFile = arcpy.GetParameterAsText(3)
outMXD = arcpy.GetParameterAsText(4)

#Update layer symbology
mxd = arcpy.mapping.MapDocument(mxdPath)
df = arcpy.mapping.ListDataFrames(mxd, dfName)[0]
updateLayer = arcpy.mapping.ListLayers(mxd, layerName)[0]
sourceLayer = arcpy.mapping.Layer(layerFile)
arcpy.mapping.UpdateLayer(df, updateLayer, sourceLayer, True)

#Save changes to new MXD and automatically open
mxd.saveACopy(outMXD)
os.startfile(outMXD)
del mxd, sourceLayer

