#coding:gbk




import urllib2
import re
import codecs
import datetime
import os

def PaCQiubaiToText(filePath,n):
    f_w=codecs.open(filePath,'w', 'utf-8')
    print '糗事百科，仅供参考'
    print filePath
    try:
        for page in range(1,10,1):
            url="http://www.qiushibaike.com/textnew/page/"+str(page)
            request=urllib2.Request(url)
            request.add_header('User-agent','Mozilla 5.10')
            response=urllib2.urlopen(request)
            content=response.read().decode('utf-8')

            reg='<h2>(.*?)</h2>.*?<div class="content">(.*?)<!--.*?-->.*?<i class="number">(.*?)</i>'
            pattern=re.compile(reg,re.S)
            results=re.findall(pattern,content)
            dataPageInfo='******************Page = %d ******************'%page
            f_w.write(dataPageInfo)
            f_w.write('\r\n')
            num=1
            for item in results:
                dataInfo='ID : %s , Host : %s , Good Number : %s'%((str(page)+'.'+str(num)),item[0],item[2])
                dataContent=item[1]
                f_w.write(dataInfo)
                f_w.write('\r\n')
                f_w.write('Content :')
                f_w.write('\r\n')
                f_w.write('\t\n')
                f_w.write(dataContent)
                f_w.write('\r\n')
                num=num+1
            print 'Page = %s Susscess !'%page
    except Exception as e:
        print 'Occur Exception Is %s'%e.message

    f_w.close()


if __name__=='__main__':

    print '***************************************'
    print 'Ihe Python Tool Start Working !'
    startTime=datetime.datetime.now()
    print '*****Start Time : %s'%startTime
    '''
    传入之指定的参数：
        filePath:文件的存放路径
        n爬虫网页的页数
    '''
    filePath=os.getcwd()
    fileName='QiuBai.txt'
    f=os.path.join(filePath,fileName)
    n=10
    PaCQiubaiToText(f,n)
    print 'Ihe Python Tool Worked OK !'
    endTime=datetime.datetime.now()
    costTime=(endTime-startTime).seconds
    print '*****Cost Time : %s s'%costTime
    print '***************************************'










