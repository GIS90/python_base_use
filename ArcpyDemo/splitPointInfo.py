__author__ = 'Administrator'
#coding:utf-8


#导入包
import re
import os
import execeptionLogging


def splitXYText(filePath):

    #遍历文件夹下的所以文件
    for f in os.listdir(filePath):
        print f,"-------------Start"


        #用try...except进行处理异常信息
        try:

            #获取文件内容
            fSour=os.path.join(filePath,f)
            fRead=open(fSour,'r')
            lines=fRead.readlines()

            #解析文件内容
            for line in lines:


                #正则判断符合条件的readline
                pattern=re.compile('v.+',re.IGNORECASE)
                m=re.match(pattern,line)
                #处理符合正则的readline进行processing
                if m!=None:
                    l1=line.split('\'')[1]
                    l3=line.split('\'')[3]+'.txt'
                    print l3
                    #遍历一个面域新建一个文件进行存储
                    fileDest=os.path.join(filePath,l3)
                    fWrite=open(fileDest,'w')
                    sXY='X'+','+'Y'
                    fWrite.write(sXY)
                    fWrite.write("\r\n")
                    lineSpList=l1.split(',')
                    #将坐标信息文件成对存储，换行
                    for i in range(0,len(lineSpList)-1,2):
                        sLine1=lineSpList[i]
                        sLine2=lineSpList[i+1]
                        sLine=sLine1+','+sLine2+"\r\n"
                        fWrite.write(sLine)
                #不符合正则的readline进行continue
                else:
                    continue
        except Exception as e:
            logInfo=e.message
            execeptionLogging.log('error',logInfo)

        print f,"------------Finish"




if __name__=='__main__':
    #设置文件的路径，全英文
    filePath=r'F:\2015_Project\ProcessFile'
    splitXYText(filePath)



