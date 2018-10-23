# -*- coding: utf-8 -*-

import os
from ConfigParser import ConfigParser


CURRENT_DIR = os.path.dirname(__file__)
cfgFile = os.path.abspath(os.path.join(CURRENT_DIR, "config.ini"))
if not os.path.exists(cfgFile):
    msg = "the config file doesn't exist " + cfgFile
    raise OSError(msg)


def getCfgItems(f=cfgFile):
    cf = ConfigParser()
    cf.read(f)
    url = cf.get('db', "url")
    user = cf.get('db', 'user')
    password = cf.get('db', 'password')
    return url, user, password
