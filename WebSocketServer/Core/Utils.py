# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/31'
"""
import datetime
import os


def GetCurStrTime():
    dt = datetime.datetime.now()
    format_time = '%Y-%m-%d %H:%M:%S'
    now = dt.strftime(format_time)
    return now


def GetCurDTTime():
    return datetime.datetime.now()


def TimeTranfsStr(dt):
    format_time = '%Y-%m-%d %H:%M:%S'
    return dt.strftime(format_time)


def GetConfig():
    __Curr_Dir = os.path.abspath(os.path.dirname(__file__))
    __Config_Dir = os.path.abspath(os.path.join(os.path.join(__Curr_Dir, '..'), 'ConfigDir'))
    __Config_FList = os.listdir(__Config_Dir)
    for f in __Config_FList:
        if f.endswith('.toml'):
            Config_FILE = os.path.abspath(os.path.join(__Config_Dir, f))
            return Config_FILE


def GetDataDir():
    __Curr_Dir = os.path.abspath(os.path.dirname(__file__))
    __Data_Dir = os.path.abspath(os.path.join(os.path.join(__Curr_Dir, '..'), 'Data'))
    return __Data_Dir



