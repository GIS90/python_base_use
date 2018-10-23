#!/usr/bin/python
# Filename: smtplib-example.py
# -*- coding: utf-8 -*-

# import module
import smtplib
import email.mime.text
from email.MIMEText import MIMEText
from email.Header import Header

#################################################
# Setting mail-server, etc
mail_host="smtp.qq.com"
mail_user="xxxxx"
mail_pass="xxxxxx"
mail_postfix="qq.com"

#################################################
# sub-function
def send_mail(to_list, subject, body):
  me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
  msg = MIMEText(body.encode('utf8'),_charset = 'utf8')
  msg['Subject'] = subject
  msg['From'] = me
  #to_list.append('cjd7749@qq.com')
  msg['To'] = ";".join(to_list)
  print '	Sending Email to : ',to_list	
  try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user, mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()
    return True
  except Exception, e:
    print str(e)
    return False

#################################################
# Main process
if __name__ == "__main__":
	# 
	mailto_list=['cjd7749@qq.com']
	content="""
	
	"""
	line = open('abc.txt').readlines()
	content = ''.join(line)	

	if send_mail(mailto_list, "subject", content):
		print "Send success!"
	else:
		print "Send failed!"

# END