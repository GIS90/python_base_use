# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: QueryTrain.py
@time: 2016/10/10 16:42
@describe: 
@remark: 
------------------------------------------------
"""

import os
import datetime
import json
import requests
from requests import Request, Session


def train_get(ts, url):
    if not isinstance(url, basestring):
        return
    try:
        resp = ts.get(url)
        print resp.status_code
        if resp.status_code == requests.codes.ok:
            resp_json = json.loads(resp.text)
            with open("query.txt", "wb") as fresp:
                fresp.write(resp.content)
    except Exception as e:
        print "train_get() occur exception: %s" % e.message
    else:
        return resp_json


def main():
    url = "https://kyfw.12306.cn/otn/leftTicket/"
    purpose_codes = "ADULT"
    from_station = "BJ"
    to_station = "TL"
    query_date = "2016-10-20"
    train_url = url + "queryT?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%sP&leftTicketDTO.to_station=%sD&purpose_codes=%s" \
                      % (query_date, from_station, to_station, purpose_codes)
    header = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }
    print train_url
    train_session = Session()
    # train_session.auth("gaoming971366@163.com", "gaoming971366")
    train_session.verify = False
    train_session.stream = True
    train_session.headers = header
    train_session.timeout = 20
    train_get(train_session, train_url)


if __name__ == "__main__":
    print "start"
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    cost_time = (end_time - start_time).seconds
    print "Running cost time is %d s." % cost_time
