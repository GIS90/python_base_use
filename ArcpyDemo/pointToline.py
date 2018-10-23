# coding:utf-8


"""
用于point类型转line类型
"""


import os
import arcpy


def pTol(fileSour, fileDest):

    print 'This Python Tool Working Point To Line !'
    arcpy.env.workspace = fileSour
    isExtistLine = os.path.exists(fileDest)
    if not isExtistLine:
        os.mkdir(fileDest)
    try:
        for data in arcpy.ListFiles('*.shp'):
            LInput_Features = data
            LOutput_FeaturesName = data.split('.')[0] + 'Line.shp'
            LOutput_Features = os.path.join(fileDest, LOutput_FeaturesName)
            Line_Field = ''
            Sort_Field = ''
            Close_Line = 'CLOSE'
            arcpy.PointsToLine_management(LInput_Features,
                                          LOutput_Features,
                                          Line_Field,
                                          Sort_Field,
                                          Close_Line)
            print data, " Point Execute Transfer To Line Success !"
    except Exception as e:
        print "Exception is :", e.message
    print "All Points To Line !"


if __name__ == '__main__':
    fileSour = r'F:\2015_Project\ProcessFile\Point'
    fileDest = r'F:\2015_Project\ProcessFile\Line'
    pTol(fileSour, fileDest)
