# -*- coding: utf-8 -*-
import arcpy
import os

arcpy.env.workspace = r"E:\mxd"
print "1A"
temppdfname = r"E:\temp\1.pdf"
print "2A"
pdfname = arcpy.env.workspace + r"\mappdf.pdf"
print "3A"
pdf = arcpy.mapping.PDFDocumentCreate(pdfname)
print "4A"
for file in os.listdir(arcpy.env.workspace):
    print "5A"
    if os.path.basename(file)[-3:] == "mxd":
        print "A"
        mxd = arcpy.mapping.MapDocument(arcpy.env.workspace + "\\" + file)
        print "A"
        arcpy.mapping.ExportToPDF(mxd, temppdfname, arcpy.mapping.ListDataFrame(mxd)[0])
        print "A"
        pdf.appendPages(temppdfname)
        print "A"
pdf.saveAndClose()
print "A"
os.remove(temppdfname)
print "F"
# del mxd,pdfname,temppdfname,pdf
