#coding:utf-8

import urllib2
import time
import codecs
import os
import threading

def timer():
    return  time.time()

def getResponses(url):
    try:
        dirPath=r'D:\Py_File\ManyThreadDemo\www.baidu.com'
        filePath=os.path.join(dirPath,(url.split('//')[1]+'.html'))
        if os.path.exists(filePath):
            print '%s Is Exist , Delete .'%filePath
            os.unlink(filePath)
        f_w=codecs.open(filePath,'w')
        request=urllib2.Request(url)
        request.add_header('User-agent','Mozilla 5.10')
        response=urllib2.urlopen(request)
        f_w.writelines(response)
        f_w.close()
        print '%s Is Generate Success ..... %s>>>'%(url,os.getpid())
    except Exception as e:
        print 'Occur Exception >>> '+e.message

if __name__=='__main__':
    urls=[
        'http://map.baidu.com',
        'http://music.baidu.com',
        'http://tieba.baidu.com',
        'http://news.baidu.com',
        'http://zhidao.baidu.com',
        'http://image.baidu.com',
        'http://baike.baidu.com'
    ]

    start=timer()
    threads=[]
    for url in urls:
        t=threading.Thread(target=getResponses,name='MyThread',args=(url,))
    end=timer()
    print '2-------------------Cost Time Is >>> %s'%(end-start)

