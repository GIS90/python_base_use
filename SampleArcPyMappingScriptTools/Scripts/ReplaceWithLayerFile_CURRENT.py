# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will replace a layer in a map document with the contents
#          of a layer file (on disk).  This script MUST be run from within
#          ArcMap because it references the CURRENT map document.
#               1) Choose layer to replace (from auto-generated list)
#               2) Path to existing layer file
#
# Note: to run the script from ArcMap either run the script tool from the
#       Catalog window from within ArcMap or add the script tool into the UI
#       via the customize dialog box [Geoprocessing Tools].

import arcpy, os

try:

    #Read input parameters from GP dialog
    layerName = arcpy.GetParameterAsText(0)
    layerFile = arcpy.GetParameterAsText(1)

    #Reference map document and layer files on disk
    mxd = arcpy.mapping.MapDocument("CURRENT")
    sourceLayer = arcpy.mapping.Layer(layerFile)

    #find layer with specified name
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.name == layerName:
                arcpy.mapping.UpdateLayer(df, lyr, sourceLayer, False)

    #Refresh the ArMap application
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    del mxd, sourceLayer

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
