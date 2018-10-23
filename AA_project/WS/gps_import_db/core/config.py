# -*- coding: utf-8 -*-
"""
解析配置文件，获取STMP，数据库，以及数据源的配置信息
"""
import inspect
import os
import pytoml
from logger import *


__CURRENT_DIR = os.path.abspath(os.path.dirname(inspect.stack()[0][1]))
__CONFIG_DIR = os.path.abspath(os.path.join(os.path.join(__CURRENT_DIR, os.path.pardir), 'config'))

__CONFIG_FILE = os.path.abspath(os.path.join(__CONFIG_DIR, "config.toml"))
tf = file(__CONFIG_FILE)
tfc = pytoml.load(tf)
# 获取发邮件配置信息
__smtp_host = tfc['SMTP']['host']
__mailTo_list = tfc['SMTP']['list']
__mail_user = tfc['SMTP']['user']
__mail_pw = tfc['SMTP']['pwd']
__mail_postfix = tfc['SMTP']['postfix']
# 获取数据库配置信息
__db_type = tfc['DATABASE']['type']
__db_server = tfc['DATABASE']['server']
__db_port = tfc['DATABASE']['port']
__db_db = tfc['DATABASE']['db']
__db_uid = tfc['DATABASE']['user']
__db_pwd = tfc['DATABASE']['pwd']
# 数据源位置
__data_source = tfc['SOURCE']['data']


def stmp_config():
    try:
        return __smtp_host, __mailTo_list, __mail_user, __mail_pw, __mail_postfix
    except Exception as e:
        logger.error("stmp_config: %s" % e.message)


def db_config():
    try:
        return __db_type, __db_server, __db_port, __db_db, __db_uid, __db_pwd
    except Exception as e:
        logger.error("db_config: %s" % e.message)


def data_config():
    try:
        return __data_source
    except Exception as e:
        logger.error("data_config: %s" % e.message)
