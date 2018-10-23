# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will export multiple map document layoutinto a single
#          output PDF file. The script is intended to run within a script tool.  There are two
#          parameters:
#               1) Select Map Documents to Append,
#               2) Output PDF.
#
# Notes: The order of the MXDs is based on how they are entered.  The MXD at the
#       top of the list is first followed by those below it.

import arcpy
import os
import string

# Read input parameters from script tool
mxdList = string.split(arcpy.GetParameterAsText(0), ";")
outPDFpath = arcpy.GetParameterAsText(1)

# Create a new PDF object to store the results
outputPDF = arcpy.mapping.PDFDocumentCreate(outPDFpath)

# Loop through each MXD in the list, export, create a temporary PDF name,
# and append to final, output PDF
for mxdPath in mxdList:
    mxd = arcpy.mapping.MapDocument(mxdPath)
    PDFPath = mxdPath[:-4] + "_temp.pdf"
    arcpy.mapping.ExportToPDF(mxd, PDFPath)
    outputPDF.appendPages(str(PDFPath))

# Save the changes and open the result automatically
outputPDF.saveAndClose()
os.startfile(outPDFpath)

# Remove variable reference to file
del outputPDF
