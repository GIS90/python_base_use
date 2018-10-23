__author__ = 'Administrator'
# -*- coding: utf-8 -*-
'''
对大文件进行分割，传入要进行分割的文件路径，名称即可
分割的方法：
            按文件大小进行分割
            按行进行分割
'''
import os

#按行进行分割，需传入大文件，分割的行数2个参数
def splitByFileRow(bigFileData,splitRowNum):
    fileSourcePath=os.path.split(bigFileData)[0]
    fileSourceName=os.path.split(bigFileData)[1]
    fileDestDir=fileSourcePath+'\ByFileRowDir'
    os.makedirs(fileDestDir)
    print fileDestDir
    fc=open(bigFileData,'r').readlines()
    print len(fc)

if __name__=="__main__":

    bigFileData=r'E:\data\GPSdat\ceshi.txt'
    print 'Start . . . . . . . . . . . . . . '
    splitRowNum=1000
    splitByFileRow(bigFileData,splitRowNum)
