# -*- coding: utf-8 -*-
"""
STMP邮件模块，主要用于发送邮件
"""

import smtplib
from email.mime.text import MIMEText
from logger import *


class SMTPMsg(object):
    def __init__(self, smtp_host, mailTo_list, mail_user, mail_pw, mail_postfix):
        """
        邮件类的初始化
        :param smtp_host:邮件类型
        :param mailTo_list: 收件人列表
        :param mail_user: 发件人用户名
        :param mail_pw: 发件人密码
        :param mail_postfix: 邮箱后缀
        :return:
        """
        self.__host = smtp_host
        self.__revlist = mailTo_list
        self.__user = mail_user
        self.__pw = mail_pw
        self.__postfix = mail_postfix

    def sendmsg(self, title, content):
        """
        发送邮件主体
        :param title: 邮件标题
        :param content: 邮件内容
        :return:
        """
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
            logger.error('SendMsg occur exception : ' + sme.message)
            return False

