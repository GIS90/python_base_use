# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/10'
"""


from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/hi')
def hi():
    return 'hi'


@app.route('/user/<user>')
def show_user(user):
    return 'User is %s .' % user


@app.route('/id/<int:id>')
def show_id(id):
    return 'Id is %d' % id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
