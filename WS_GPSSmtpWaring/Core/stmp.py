# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/30'
"""

import smtplib
from email.mime.text import MIMEText
from Log import *


class SMTPMsg(object):
    def __init__(self, smtp_host, mailTo_list, mail_user, mail_pw, mail_postfix):
        self.__host = smtp_host
        self.__revlist = mailTo_list
        self.__user = mail_user
        self.__pw = mail_pw
        self.__postfix = mail_postfix

    def sendmsg(self, title, content):
        host = "<" + self.__user + "@" + self.__postfix + ">"
        meg = MIMEText(content, _subtype='plain')
        meg["Accept-Language"] = "zh-CN"
        meg["Accept-Charset"] = "ISO-8859-1,utf-8"
        meg['Subject'] = title
        meg['From'] = host
        meg['To'] = ";".join(self.__revlist)
        try:
            server = smtplib.SMTP()
            server.connect(self.__host)
            server.login(self.__user, self.__pw)
            server.sendmail(host, self.__revlist, meg.as_string())
            server.close()
            return True
        except Exception as sme:
            Log.debug('SendMsg occur Exception : ' + sme.message)
            return False


if __name__ == '__main__':
    smtp_host = "smtp.163.com"
    mailTo_list = ['605760635@qq.com', '154589878@qq.com']
    mail_user = "gaoming971366"
    mail_pw = "625125301"
    mail_postfix = "163.com"
    sm = SMTPMsg(smtp_host, mailTo_list, mail_user,mail_pw, mail_postfix)
    title = 'GPS 段数'
    content = """
    192.168.1.77服务器GPS数据源已断，具体时间为：%s
    """
    print sm.SendMsg(title, content)
