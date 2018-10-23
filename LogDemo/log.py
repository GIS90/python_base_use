# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/27'
"""

import logging
import inspect
import os
import sys


print inspect.stack()[0][1]
print inspect.stack()
print inspect.trace()
print inspect.getsourcefile(os)


