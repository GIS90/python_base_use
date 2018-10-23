#coding:utf-8



import os
import codecs

def transferToUTF8(filePath):
    if not os.path.exists(filePath):
        return 'File Is NO Exist.'
    if os.path.isfile(filePath):
        fileTransferToUTF8(filePath)
    elif os.path.isdir(filePath):
        dirTransferToUTF8(filePath)


def fileTransferToUTF8(filePath):
    fileContent=open(filePath,'r').read()
    try:
        newFileContent=fileContent.decode().encode('utf-8')
        os.unlink(filePath)
        codecs.open(filePath,'w','utf-8').write(newFileContent)
    except Exception as e:
        print 'File Transfer Failure'

def dirTransferToUTF8(filePath):
    pass

if __name__=='__main__':
    filePath=r'E:\ceshi.txt'
    transferToUTF8(filePath)
    print 1






