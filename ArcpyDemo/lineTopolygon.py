# coding:utf-8


"""
用于point类型转line类型
"""

import os
import arcpy


def lToP(fileSour, fileDest):

    print 'This Python Tool Working Line To Polygon !'
    arcpy.env.workspace = fileSour
    isExtistPolygon = os.path.exists(fileDest)
    if not isExtistPolygon:
        os.mkdir(fileDest)

    try:
        for data in arcpy.ListFiles('*.shp'):
            PInput_Features = data
            POutput_FeaturesName = data.split('L')[0] + 'Polygon.shp'
            POutput_Features = os.path.join(fileDest, POutput_FeaturesName)
            cluster_tolerance = '0.00000001'
            attributes = 'NO_ATTRIBUTES'
            label_features = ''
            arcpy.FeatureToPolygon_management(PInput_Features,
                                              POutput_Features,
                                              cluster_tolerance,
                                              attributes,
                                              label_features)
            print data, " Line Execute Transfer To Polygon Success !"
    except Exception as e:
        print "Exception is :", e.message

    print "All Lines To Polygon !"


if __name__ == '__main__':
    fileSour = r'F:\2015_Project\ProcessFile\Line'
    fileDest = r'F:\2015_Project\ProcessFile\Polygon'
    lToP(fileSour, fileDest)
