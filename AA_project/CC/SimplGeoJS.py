# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/18'
"""

import os
import json
import contextlib


def SimplifyJS(path):
    assert isinstance(path, basestring)
    data = []
    if not os.path.exists(path):
        return False, '%s is not exist .' % path
    FILE_LIST = os.listdir(path)
    for f in FILE_LIST:
        if f.endswith('.js'):
            js = os.path.abspath(os.path.join(path, f))
            with contextlib.closing(open(js)) as js_open:
                js_cont = json.load(js_open)
                print js_cont

    return True, 'Success'


if __name__ == '__main__':
    JS_PATH = r'E:\data\cc_js'
    rlt, info = SimplifyJS(JS_PATH)
    print info
