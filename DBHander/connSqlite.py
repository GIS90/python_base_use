# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/8/4'
"""

import sqlite3


con = sqlite3.connect(r"C:\Users\localhost\Documents\Tencent Files\625125301\Msg3.0.db")

cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())