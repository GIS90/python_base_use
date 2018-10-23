# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/12'
"""

from flask import Flask
app = Flask(__name__)


@app.route('/hi')
def hi():
    return 'hi'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20000, debug=True)
