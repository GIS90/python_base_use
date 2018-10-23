# -*- coding: utf-8 -*-

import xlwt
import os


def ReadTxt(txt):
    print 1
    if not os .path.exists(txt):
        return -1, 'Text File Not Exist .'
    fCont = open(txt, 'r').readlines()
    for line in fCont:
        print line



def WriteXls():
    pass


if __name__ == '__main_':
    txt = r'E:\data\txt\receive.2016-02-29.txt'
    print ReadTxt(txt=txt)
    fCont = open(txt).read()
    for line in fCont:
        print line
