# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will loop through every page layout element and apply the
#          specified X and Y shifts to each element. The script is helpful for
#          repositioning the elements so they are better aligned with the printer
#          margins/page.  This script is intended to run as a script tool and
#          has four parameters:
#               1) Input map document,
#               2) X shift,
#               3) Y shift,
#               4) Output map document.

import arcpy, os
import arcpy.mapping as MAP

#Read parameters from dialog
mxdPath = arcpy.GetParameterAsText(0)
xShift = arcpy.GetParameterAsText(1)
yShift = arcpy.GetParameterAsText(2)
outPath = arcpy.GetParameterAsText(3)

#Reference the map document
MXD = MAP.MapDocument(mxdPath)

#Loop through each page layout element and shift the x and y values
for elm in MAP.ListLayoutElements(MXD):
    elm.elementPositionX = elm.elementPositionX + float(xShift)
    elm.elementPositionY = elm.elementPositionY + float(yShift)

#Save changes to new MXD and automatically open
MXD.saveACopy(outPath)
os.startfile(outPath)
