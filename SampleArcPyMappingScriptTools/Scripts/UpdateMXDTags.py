# Author:  ESRI
# Date:    July 5 , 2010
# Version: ArcGIS 10.0
# Purpose: This script will iterate through each layer in a map document and add
#          the name of each layer as a tag value to the MXD.  The tags are
#          searchable via the search dialog and then MXDs can be identified 
#          based on the layers they contain.  The script is intended to run
#          from a script tool that requires two input parameters:
#               1) Browse to an existing MXD.
#               2) Browse to and name an output MXD.

#          The resulting MXD will automatically open.

import arcpy, os

try:

    #Read parameters from dialog
    mxdPath = arcpy.GetParameterAsText(0)
    outputMXD = arcpy.GetParameterAsText(1)

    #Reference Map Document
    mxd = arcpy.mapping.MapDocument(mxdPath)

    #Generate unique, sorted list of layer names
    layers = arcpy.mapping.ListLayers(mxd)
    layerList = []
    for lyr in layers:
        if not lyr.isGroupLayer:
            layerList.append(lyr.name)
    uniqueList = list(set(layerList))
    uniqueList.sort()

    #Update map document tags
    tagList = ",".join(uniqueList)  
    mxd.tags = tagList

    #save map document
    mxd.saveACopy(outputMXD)
    os.startfile(outputMXD)

    del mxd
    
except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))



