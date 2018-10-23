# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/30'
"""


from Core.AnlyConfigInfo import *
from Core.SendStmp import *
from Core.DBHand import *
from Core.Utils import *
from Core.Log import *
from time import strftime, localtime
import codecs


def Main():
    try:
        dbtype, server, port, dedb, uid, pwd = GetDBConfig()
        query = GetQUERYConfig()
        mail_host, mail_list, mail_user, mail_pw, mail_postfix = GetSMTPConfig()
        db = DBHand(dbtype, server, port, dedb, uid, pwd)
        sm = SMTPMsg(mail_host, mail_list, mail_user, mail_pw, mail_postfix)
        cur_time = GetCurStrTime()
        year = strftime("%Y", localtime())
        mon = strftime("%m", localtime())
        up_mon = int(mon) - 1
        if up_mon < 10:
            up_mon = "0" + str(up_mon)
        day = strftime("%d", localtime())
        query_time_start = str(year) + "-" + str(up_mon) + "-" + str(day) + " 00:00:00"
        query_time_end = str(year) + "-" + str(mon) + "-" + str(day) + " 00:00:00"
        f_name, f_path = GetFILEConfig()
        f_name = f_name + year + str(up_mon) + '.txt'
        fo = os.path.join(f_path, f_name)
        fw = codecs.open(fo, 'w', 'utf-8')
        if db.open():
            query_sql = query % (query_time_start, query_time_end)
            query_type = 2
            print query_sql
            rlt = db.handle(query_type, query_sql)
            title = 'FcdT_Link15m数据情况'
            content = """
    192.168.1.77服务器一次计算结果FcdT_Link15m，生成文件%s，具体时间为：%s 至 %s 。



                                                                通知方式：邮件报警
                                                                通 知 人：高明亮
                                                                通知时间：%s

            """ % (query_time_start, query_time_end, f, cur_time)
            fw.write("time, linkid, speed, length, sampleNum")
            for row in rlt:
                fw.write('\r\n')
                fw.write(str(row))
            sm.SendMsg(title, content)
            msg = 'FcdT_Link15m query success，send mail message.'
            return True, msg
    except Exception as ee:
        Log.debug("Main occur Exception : %s ." % ee.message)
        return False, "Main occur error"
    finally:
        db.close()
        fw.close()

if __name__ == '__main__':

    try:
        rlt, info = Main()
        if rlt:
            print '检查时间：%s , 检查结果为：%s' % (GetCurStrTime(), info)
        else:
            print '检查时间：%s，程序发生错误，请查看日志：%s' % (GetCurStrTime(), info)
    except Exception as me:
        Log.debug('Main occur Exception : %s' % me.message)

