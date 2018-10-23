# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/21"


class HeJie(object):
    def __init__(self):
        self.BHW = "BaoHongWei"
        self.GML = "GaoMingLiang"
        self.LQ = "LiQian"
        self.SYH = "SunYaHui"
        self.QYJ = "QinYingJie"

    def enjoy(self):
        pass

    def hejiu(self):
        pass

    def close(self):
        pass


import random
import shapefile
import struct
import sys





if __name__ == "__main__":

    enjoy = {1: "喝一杯",
             2: "脱一件衣服",
             3: "",
             4: "选择",
             5: "",
             6: "",
             7: "",
             8: "",
             9: "",
             10: ""}
    rand = random.randint(1, 4)
    print rand
    for key, value in enjoy.items():
        if key == rand:
            print value
