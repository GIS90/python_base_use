# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/10'
"""

from flask import Flask, render_template, request
import MySQLdb as mysql
import json


# con = mysql.connect(user='root', passwd='123456', host='localhost', db='test')
#
# con.autocommit(True)
# cur = con.cursor()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/data')
# def data():
#     sql = 'select * from ceshi'
#     cur.execute(sql)
#     arr = []
#     for i in cur.fetchall():
#         arr.append([i[1] * 1000, i[0]])
#     return json.dumps(arr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
