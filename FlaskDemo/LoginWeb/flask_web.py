# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/18'
"""


import os
import contextlib
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


app = Flask(__name__)
app.config.update(dict(
    DB='pam.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USER='gml',
    PWD='123456'
))
app.config.from_envvar('FLASK_SETTINGS', silent=True)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config["DB"])


def init_db():
    with contextlib.closing(connect_db()) as db:
        with app.open_resource('init.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exeception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


@app.route('/')
def show():
    entries = None
    cursor = g.db.execute('select title, text from entries order by id desc')
    for row in cursor.fetchall():
        entries = dict(title=row[0], text=row[1])
    return render_template('show.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.fromp['username'] != app.config['USER']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['loggin_in'] = True
            flash('We are Logged in')
            return redirect(url_for('show'))
        return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('We are Logged out')
    return redirect(url_for('show'))


if __name__ == '__main__':
    print 'Start Flask'
    CUR_DIR = os.path.dirname(__file__)
    FILE_LIST = os.listdir(CUR_DIR)
    if app.config['DB'] not in FILE_LIST:
        init_db()
    app.run(host='0.0.0.0', port=9090)


