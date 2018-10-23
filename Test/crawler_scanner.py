# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/31'
"""

import os
import urllib2
import threading
import Queue
import time
import random

q = Queue.Queue()  # Queue产生一个队列，有3种类型队列 默认用 FIFO队列
threading_num = 5  # 开启5个线程

# 扫描本地IP或域名
domain_name = "http://127.0.0.1"
# 百度蜘蛛UA
Baidu_spider = "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
# 不需要的文件过滤列表
exclude_list = ['.jpg', '.gif', '.css', '.png', '.js', '.scss']

proxy_list = [  # 代理服务器，可能已经失效，换为自己的
    {'http': '117.28.254.130:8080'},
    {'http': '118.144.177.254:3128'},
    {'http': '113.118.211.152:9797'},
]

# 打开字典文件，开始过滤不需要的文件路径
with open("/home/leo/app_txt/wordpress.txt", "r") as lines:
    for line in lines:
        line = line.rstrip()
        if os.path.splitext(line)[1] not in exclude_list:
            q.put(line)  # 将line传入到队列 q 中


# 扫描器方法
def crawler():
    while not q.empty():  # 循环
        path = q.get()  # 将line从队列q中取出来

        url = "%s%s" % (domain_name, path)  # 组合url地址，用于下一步提交

        random_proxy = random.choice(proxy_list)  # 随机使用一个代理服务器
        proxy_support = urllib2.ProxyHandler(random_proxy)
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)

        headers = {}
        headers['User-Agent'] = Baidu_spider  # 蜘蛛的头部信息
        # 玩蛇网 www.iplaypython.com

        request = urllib2.Request(url, headers=headers)

        try:
            response = urllib2.urlopen(request)
            content = response.read()

            if len(content):  # 内容不为空的情况下返回状态码、路径
                print "Status [%s]  - path: %s" % (response.code, path)

            response.close()
            time.sleep(1)  # 休息一会儿，防止速度过快连接数过大被封掉IP
        except urllib2.HTTPError as e:
            # print e.code, path
            pass  # 异常处理，先暂时pass掉


if __name__ == '__main__':
    # 创建多线程并指明函数的入口为crawler，以后还可以传参进去
    for i in range(threading_num):
        t = threading.Thread(target=crawler)
        t.start()
