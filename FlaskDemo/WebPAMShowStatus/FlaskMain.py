# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/12'
"""

from flask import Flask, request
# 设置static, template文件夹目录
staticPath = r'D:\Py_file\FlaskDemo\WebPAMShowStatus\static'
templatePath = r'D:\Py_file\FlaskDemo\WebPAMShowStatus\templates'
app = Flask(__name__, static_folder=staticPath, template_folder=templatePath)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/hi/')
def hi():
    return 'Hi'


@app.route('/user/<user>')
def show_user(user):
    return 'User is %s .' % user


@app.route('/id/<int:idV>')
def show_id(idV):
    return 'Id is %d' % idV


@app.route('/map/')
def mapShow():
    from flask import render_template
    return render_template('barChart.html')


@app.route('/login', methods=['GET', 'POST'])
def login_method():
    if request.method == 'POST':
        print 'post'
    else:
        print 'get'


if __name__ == '__main__':
    # 调试
    app.debug = False
    app.run(host='0.0.0.0', port=8888)

    # 处理Flask异常
    accMail = ['gaoming971366@163.com']
    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler('127.0.0.1',
                                   'server-error@example.com',
                                    accMail,
                                   'YourApplication Failed')
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
        print 'Occur ERROR'
