# -*- coding:utf-8 -*-



import smtplib
from email.mime.text import MIMEText



class SNMPManage(object):

    SMTPHost = "smtp.163.com"
    mailToList = ['625125301@qq.com']
    mailUser = "gaoming971366"
    mailPw = "625125301"
    mailPostfix = "163.com"


    def sendMessage(title, content):
        host = "高明亮" + "<" + SNMPManage.mailUser + "@" + SNMPManage.mailPostfix + ">"
        meg = MIMEText(content, _subtype='plain')
        meg["Accept-Language"] = "zh-CN"
        meg["Accept-Charset"] = "ISO-8859-1,utf-8"
        meg['Subject'] = title
        meg['From'] = host
        meg['To'] = ";".join(SNMPManage.mailToList)

        try:
            server = smtplib.SMTP()
            server.connect(SNMPManage.SMTPHost)
            server.login(SNMPManage.mailUser, SNMPManage.mailPw)
            server.sendmail(host, SNMPManage.mailToList, meg.as_string())
            server.close()
            return True
        except Exception as e:
            print e.message
            return False
