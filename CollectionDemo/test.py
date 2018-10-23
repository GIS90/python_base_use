# -*- encoding: utf-8 -*-


# 导入包
import os
import urllib
import re
import time
import datetime


# 显示下载进度
def sch(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per


# 打开url并读取里面内容
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read().decode("utf-8")
    print html
    return urllib.urlopen(url).read().decode("utf-8")


# 下载html里面的图片
def getImage(html):
    # 正则判断是否为图片
    reg = r'src="(.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    print imglist

    # 创建存放图片文件夹
    x = time.localtime()
    filename = str(x.__getattribute__("tm_mon")) + "-" + str(x.__getattribute__("tm_mday")) + "-" + str(
        x.__getattribute__("tm_hour"))
    picpath = "E:/test/" + filename

    if (os.path.exists(picpath)):
        os.rmdir(picpath)
    else:
        os.makedirs(picpath)
    i = 0
    # 下载图片
    for imgurl in imglist:
        name = "%s.jpg" % i
        pic = picpath + "/" + name
        print "The photos url site is:", imgurl
        print "The photos location is:" + pic
        urllib.urlretrieve(imgurl, pic, sch)
        print "-----------------------------------"
        i = i + 1
        time.sleep(10)
    return imglist


if __name__ == "__main__":
    print "*************************************************************"
    starttime = datetime.datetime.now()
    print u"开始时间：", starttime
    url = "http://huaban.com/favorite/beauty/?qq-pf-to=pcqq.temporaryc2c"

    html = getHtml(url)

    print getImage(html)

    endtime = datetime.datetime.now()
    print u"结束时间：", endtime
    d = endtime - starttime
    print u"总共花费时间是：", d
    print "**************************************************************"
