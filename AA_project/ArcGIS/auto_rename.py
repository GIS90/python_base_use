# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    atuomate rename files of the designated folder that contains history, live
    rename update rate is one day refer to current time of the server
------------------------------------------------
"""
import os
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/9"


def re_live():
    pass


def re_history():
    pass


def main():
    pass


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser("start exe:")
    parser.add_argument("-m", "--mode", default="file", help="you must specify which to monitor, dir or file?")
    args = parser.parse_args()
    print args






