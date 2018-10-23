# -*- coding: utf-8 -*-

"""
Author: cuiheng
Create Date: 7/6/15
FILE: calc
DESCRIPTION: 
"""
import os


def main(fileName):
    print "we will check the file %s" % fileName
    fileName = os.path.abspath(fileName)
    if not os.path.exists(fileName):
        print "file name not exist %s" % fileName
        return
    result = {}
    with open(fileName) as f:
        lines = f.readlines()
        for l in lines:
            if not l:
                break
            carID = l.split(",")[0]
            if carID not in result:
                result[carID] = 1
    print len(result)


if __name__ == '__main__':
    import sys

    main(sys.argv[1])
