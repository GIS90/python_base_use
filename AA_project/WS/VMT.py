# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
calcueate vmt value
class = 1, 2, 5

------------------------------------------------
"""
import arcpy
import os
import sys
try:
    import cPickle as pickle
except:
    import pickle

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/16"


HEXIN_IDS = [301, 302]
ROAD_CLASSES = [1, 2, 5]

shape = r'E:\data\ws\ws_hexin_linkgeo\linkgeo.shp'
fields = ['hexin_id', 'ROADCLASS', 'Length']
road_legths = {}


def check(shape):
    assert isinstance(shape, basestring)

    if not os.path.exists(shape):
        print '%s is not exist' % shape
        sys.exit(1)
    if not os.path.isfile(shape):
        print '%s is not file' % shape
        sys.exit(1)


def main():
    check(shape)
    with arcpy.da.SearchCursor(shape, fields) as cursor:
        if cursor:
            for hexin_id in HEXIN_IDS:
                for road_class in ROAD_CLASSES:
                    lengths = 0
                    for ft in cursor:
                        ft_id = int(ft[0])
                        ft_class = int(ft[1])
                        ft_length = float(ft[2])

                        if ft_id == hexin_id and ft_class == road_class:
                            lengths += ft_length
                    did = str(int(hexin_id)) + '_' + str(int(road_class))
                    road_legths[did] = lengths
                    cursor.reset()
        else:
            print '%s data is error'

    with open('road_lengths.txt', 'w') as f:
        for k, v in road_legths.items():
            line = k + ": " + str(v)
            f.writelines(line)
            f.write('\n')


if __name__ == '__main__':
    main()
    print 'end'


