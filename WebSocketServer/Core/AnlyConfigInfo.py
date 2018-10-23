# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/30'
"""


import pytoml
import os


__Curr_Dir = os.path.abspath(os.path.dirname(__file__))
__Config_Dir = os.path.abspath(os.path.join(os.path.join(__Curr_Dir, '..'), 'ConfigDir'))
__Config_FList = os.listdir(__Config_Dir)
for f in __Config_FList:
    if f.endswith('.toml'):
        Config_FILE = os.path.abspath(os.path.join(__Config_Dir, f))
        tf = file(Config_FILE)
        tfc = pytoml.load(tf)
        # 获取发邮件配置信息
        __smtp_host = tfc['SMTP']['smtp_host']
        __mailTo_list = tfc['SMTP']['mailTo_list']
        __mail_user = tfc['SMTP']['mail_user']
        __mail_pw = tfc['SMTP']['mail_pw']
        __mail_postfix = tfc['SMTP']['mail_postfix']
        # 获取数据库配置信息
        __DB_type = tfc['DATABASE']['DB_type']
        __DB_server = tfc['DATABASE']['DB_server']
        __DB_port = tfc['DATABASE']['DB_port']
        __DB_db = tfc['DATABASE']['DB_db']
        __DB_uid = tfc['DATABASE']['DB_uid']
        __DB_pwd = tfc['DATABASE']['DB_pwd']


def GetSMTPConfig():
    return __smtp_host, __mailTo_list, __mail_user, __mail_pw, __mail_postfix


def GetDBConfig():
    return __DB_type, __DB_server, __DB_port, __DB_db, __DB_uid, __DB_pwd
