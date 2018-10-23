# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will append multiple PDFs into a single output PDF file.
#          The script is intended to run within a script tool.  There are two
#          parameters:
#               1) Select PDF Files to Append,
#               2) Output PDF.
#
#Notes: The order of the PDFs is based on how they are entered.  The PDF at the
#       top of the list is first followed by those below it.

import arcpy, os, string

#Read input parameters from script tool
PDFList = string.split(arcpy.GetParameterAsText(0), ";")
outPDFpath = arcpy.GetParameterAsText(1)

#Create a new PDF object to store the results
outputPDF = arcpy.mapping.PDFDocumentCreate(outPDFpath)

#Loop through and append each PDF in the list
for eachPDF in PDFList:
    outputPDF.appendPages(str(eachPDF))

#Save the changes and open the result automatically   
outputPDF.saveAndClose()
os.startfile(outPDFpath)

#Remove variable reference to file
del outputPDF

