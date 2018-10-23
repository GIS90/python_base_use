#coding:utf-8




import gzip
import os
import shutil
# filePath=r'E:\WorkingLogg'
# list=os.listdir(filePath)
# fd=r'E:\WorkingLogg\test.gz'
# gz=gzip.open(fd,'wb')
# for i in list:
#     f=os.path.join(filePath,i)
#     content=open(f,'rb').read()
#     gz.write(content)
import tarfile

#创建压缩包名
filePath=r'E:\WorkingLogg'
tar = tarfile.open(r"E:\WorkingLogg\tartest.tar.gz","w:gz")
#创建压缩包
for root,dir,files in os.walk("filePath"):
    for file in files:
        fullpath = os.path.join(root,file)
        tar.add(fullpath)
tar.close()
# print 1