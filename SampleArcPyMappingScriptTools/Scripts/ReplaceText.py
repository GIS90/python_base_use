# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will perform a search and replace on page layout text
#          elements. There are options to match case and/or find exact matches.
#          This script is intended to run as a scrip tool and requires three
#          parameters (and two optional parameters):
#               1) Input map document,
#               2) Find string,
#               3) Replace string,
#               4) Match case,
#               5) Match entire string.

import arcpy, string, os 

#Read input parameters from script tool
mxdPath = arcpy.GetParameterAsText(0)
oldText = arcpy.GetParameterAsText(1)
newText = arcpy.GetParameterAsText(2)
case = arcpy.GetParameter(3)
exact = arcpy.GetParameter(4)
outputMXD = arcpy.GetParameterAsText(5)

try:
    #Referent the map document
    mxd = arcpy.mapping.MapDocument(mxdPath)         

    #Find all page layout text elements
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):     
        if exact:
            if case:
                if oldText == elm.text:
                    elmText = elm.text.replace(oldText, newText)
                    elm.text = elmText
            else:
                if oldText.upper() == elm.text.upper():
                    elmText = elm.text.upper().replace(oldText, newText)
                    elm.text = elmText   
        else:
            if case:
                if oldText in elm.text:
                    elmText = elm.text.replace(oldText, newText)
                    elm.text = elmText
            else:
                if oldText.upper() in elm.text.upper():
                    elmText = elm.text.upper().replace(oldText, newText)
                    elm.text = elmText                  
    mxd.saveACopy(outputMXD)
    os.startfile(outputMXD)

    del mxd

except Exception, e:
    import traceback
    map(arcpy.AddError, traceback.format_exc().split("\n"))
    arcpy.AddError(str(e))
