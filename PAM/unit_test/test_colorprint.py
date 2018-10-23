# -*- coding: utf-8 -*-

import os
DIR = os.path.dirname(__file__)
print DIR
PARENT_DIR = os.path.join(DIR, "..")
print PARENT_DIR
PARENT_DIR = os.path.abspath(PARENT_DIR)
print PARENT_DIR
import sys
sys.path.append(PARENT_DIR)
from core.ColorPrint import *



msg='颜色'
print WindowsCMDColorPrint().printBlue(msg)