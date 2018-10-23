# -*- coding: utf-8 -*-


import unittest
from core.Util import *
from unittest import *


class test_util(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLog(self):
        a = runLocalCmd("dir C:\\")
        print a

    # def testCompress(self):
    #     filePath = r'D:\Oracle\oracle.docx'
    #     dirPath = r'D:\Oracle'
    #     gzName = 'test.gz'
    #     gzPath = 'D:\\'
    #     print(compress(filePath))
    #     print(compress(filePath, gzName))
    #     print(compress(filePath, outputFolder=gzPath))
    #     print(compress(filePath, gzName, gzPath))
    #     print(compress(dirPath))
    #     print(compress(dirPath, gzName))
    #     print(compress(dirPath, outputFolder=gzPath))
    #     print(compress(dirPath, gzName, gzPath))
    #     pass
    def testCompressByTarfile(self):
        filePath = r'D:\Oracle\oracle.docx'
        dirPath = r'D:\Oracle'
        gzName = 'test.gz'
        gzPath = 'D:\\'
        print(compressByTarfile(filePath))
        print(compressByTarfile(filePath, gzName))
        print(compressByTarfile(filePath, outputFolder=gzPath))
        print(compressByTarfile(filePath, gzName, gzPath))
        print(compressByTarfile(dirPath))
        print(compressByTarfile(dirPath, gzName))
        print(compressByTarfile(dirPath, outputFolder=gzPath))
        print(compressByTarfile(dirPath, gzName, gzPath))


if __name__ == '__main__':
    unittest.main()