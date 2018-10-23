# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will print one or more map documents to a local printer.
#          The script is intended to run within a script tool.  There are two
#          parameters:
#               1) Select Map Documents to Print,
#               2) Select Output Printer (auto populated using a validation script)
#
#Notes: The print order of the MXDs is based on how they are entered.  The MXD
#       at the top of the list is first followed by those below it.

import arcpy, string

#Read input parameters from script tool
mxdPath = arcpy.GetParameterAsText(0)
pageList = string.split(arcpy.GetParameterAsText(3), ";")
printer = arcpy.GetParameterAsText(4)

#Reference the map and the data driven page object
mxd = arcpy.mapping.MapDocument(mxdPath)
ddp = mxd.dataDrivenPages
for eachPage in pageList:
    arcpy.AddMessage(str(eachPage))
    pageID = ddp.getPageIDFromName(str(eachPage.strip("'")))
    ddp.currentPageID = pageID
    ddp.printPages(printer, "CURRENT")

#Remove variable reference to file
del mxd
