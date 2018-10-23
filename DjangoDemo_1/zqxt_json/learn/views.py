#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-26 12:32:06
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
# @Version : 0.0.1
from __future__ import unicode_literals
from django.shortcuts import render
import json


def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}

    return render(request, 'home.html', {'List': json.dumps(List), 'Dict': json.dumps(Dict)})
