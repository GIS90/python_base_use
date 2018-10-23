# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from __future__ import division

import sys
import time

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/20"


def rev_one(s):
    s_list = [x for x in s.split(' ')]
    s_list_rev = []
    for index in range((len(s_list) - 1), -1, -1):
        s_list_rev.append(s_list[index])

    s_new = ' '.join(s_list_rev)

    print 'transfer head: %s' % s
    print 'transfer rear: %s' % s_new



s = 'A fox has jumped into the river'
# rev_one(s)

