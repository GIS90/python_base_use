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
import arcpy.mapping as MAP

#Read input parameters from script tool
MXDList = string.split(arcpy.GetParameterAsText(0), ";")
printer = arcpy.GetParameterAsText(1)

#Loop through each MXD and print
for MXDPath in MXDList:
    MXD = MAP.MapDocument(MXDPath)
    MAP.PrintMap(MXD, printer)

#Remove variable reference to file
del MXD
