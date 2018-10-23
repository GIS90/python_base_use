# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/29'
"""
import os
import yaml


Curr_Dir = os.path.abspath(os.path.dirname(__file__))
Config_Dir = os.path.abspath(os.path.join(os.path.join(Curr_Dir, '..'), 'ConfigDir'))
Config_FList = os.listdir(Config_Dir)
for f in Config_FList:
    if f.endswith('.yaml'):
        Config_YAML = os.path.abspath(os.path.join(Config_Dir, f))
        with open(Config_YAML) as fy:
            content = fy.read()
            yc = yaml.load(content)
            DB_DRIVER = '{SQL Server}'
            DB_TYPE = yc['DATABASE']['TYPE']
            DB_SERVER = yc['DATABASE']['SERVER']
            DB_PORT = yc['DATABASE']['PORT']
            DB_DB = yc['DATABASE']['DB']
            DB_UID = yc['DATABASE']['UID']
            DB_PWD = str(yc['DATABASE']['PWD'])
            SQL_TYPE = int(yc['SQL']['TYPE'])
            SQL_CONTENT = yc['SQL']['CONTENT']
            RF_TYPE = yc['RF']['TYPE']
            RF_NAME = yc['RF']['NAME']
            RF_PATH = yc['RF']['PATH']
    elif f.endswith('.js'):
        Config_Js = os.path.abspath(os.path.join(Config_Dir, f))

