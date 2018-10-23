# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Summary: This script will add a layer file into a map document. The script
#          must be run from within ArcMap because it references the CURRENT
#          map document.  The purpose of the script is to create a user
#          friendly tool that allows users to simply add a layer from a list
#          of existing layer files all stored in a common location. A validation
#          script is used to automatically populate two of the parameters.
#          The parameters are:
#               1) Browse to a folder that contains layer files. This could be
#                  hard coded within the validation script eliminating the need
#                  for entering this parameter.
#               2) Select a layer file from the list.  This is auto populated
#                  using a validation script.
#               3) Select a data frame.  This is also auto populated using a 
#                  validation script.
#               4) Select one of 3 placement positions.
#
# Note: This script tool will only work if background processing is disabled.
#       because CURRENT is being used.
# Note: To run the script from ArcMap either run the script tool from the
#       Catalog window from within ArcMap or add the script tool into the UI
#       via the customize dialog box [Geoprocessing Tools].

import arcpy

try:
    #Read parameters from dialog
    folderLocation = arcpy.GetParameterAsText(0)
    layerFile = arcpy.GetParameterAsText(1)
    dfName = arcpy.GetParameterAsText(2)
    position = arcpy.GetParameterAsText(3)

    #Reference map document from within ArcMap
    mxd = arcpy.mapping.MapDocument("CURRENT")

    #Reference the layer file on disk and data frame
    addLayer = arcpy.mapping.Layer(layerFile)
    df = arcpy.mapping.ListDataFrames(mxd, dfName)[0]

    #Add layer file
    arcpy.mapping.AddLayer(df, addLayer, position)

    #Refresh TOC and ActiveView
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    del mxd, addLayer

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
