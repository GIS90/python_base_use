# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/12'
"""


import sqlite3
import os
from flask import Flask, render_template, flash, redirect, request, url_for, session, g, abort


staticPath = r'D:\Py_file\FlaskDemo\PAM_Web\static'
templatesPath = r'D:\Py_file\FlaskDemo\PAM_Web\templates'
app = Flask(__name__)
app.config.update(dict(
    DB='PAM.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USER='gml',
    PWD='123456'
))
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def init_db():
    from contextlib import closing
    with closing(connect_db()) as db:
        with app.open_resource('create.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def connect_db():
    return sqlite3.connect(app.config['DB'], timeout=10)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


@app.route('/')
def hello():
    return 'Hello Flask'


if __name__ == '__main__':
    currFileList = os.listdir(os.path.dirname(__file__))
    dbName = 'PAM.db'
    if dbName not in currFileList:
        init_db()
    # app.debug = True
    # app.run(host='0.0.0.0', port=9999)




