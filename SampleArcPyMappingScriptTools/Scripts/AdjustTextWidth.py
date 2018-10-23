# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will adjust the width of a text element to fit within a
#          specified width. It demonstrates how to dynamically control text element
#          widths using format tags.  This script is intended to run as script
#          tool within ArcMap because it references the "current" map document.
#
#          There are three input parameters:
#               1) Select a text element to modify (auto populated using a validation script)
#               2) A new string to assign to the text element
#               3) A new width to assign to the text element

import arcpy

#Read input parameters from script tool
elmName = arcpy.GetParameterAsText(0)
elmText = arcpy.GetParameterAsText(1)
elmWidth = arcpy.GetParameterAsText(2)

try:

    #Reference the current map document
    mxd = arcpy.mapping.MapDocument("CURRENT")         

    #Find the appropriate text element, start with a size of 100 and reduce until the text fits
    #the specified width.
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if elm.name == elmName:
            x = 100
            elm.text = "<FNT name=\"Arial\" size=\"" + str(x) + "\">" + elmText + "</FNT>"
            while elm.elementWidth > float(elmWidth):
                elm.text = "<FNT name=\"Arial\" size=\"" + str(x) + "\">" + elmText + "</FNT>"
                x = x - 1

    #Refresh the display
    arcpy.RefreshActiveView()
                
except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
