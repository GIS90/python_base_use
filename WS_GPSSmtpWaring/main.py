# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/30'
"""

from Core.DBHand import *
from Core.Log import *
from Core.SendStmp import *
from Core.Utils import *
from WebSocketServer.Core.AnlyConfigInfo import *


def Main():
    try:
        dbtype, server, port, dedb, uid, pwd = GetDBConfig()
        query_num, query_time = GetQUERYCOnfig()
        mail_host, mail_list, mail_user, mail_pw, mail_postfix = GetSMTPConfig()
        db = DBHand(dbtype, server, port, dedb, uid, pwd)
        sm = SMTPMsg(mail_host, mail_list, mail_user, mail_pw, mail_postfix)
        cur_time = GetCurStrTime()
        query_time_strat = TimeTranfsStr(GetCurDTTime() - datetime.timedelta(minutes=15))
        query_time_end = TimeTranfsStr(GetCurDTTime() - datetime.timedelta(minutes=10))
        if db.open():
            query_sql = query_num % (query_time_strat, query_time_end)
            quert_type = 1
            rlt_num = db.handle(quert_type, query_sql)
            if int(rlt_num) == 0:
                rlt_time = db.handle(quert_type, query_time)
                title = 'GPS 段数'
                content = """
        192.168.1.77服务器GPS数据源已断，接收数据量为0，具体时间为：%s 。



                                                                    通知方式：邮件报警
                                                                    通 知 人：高明亮
                                                                    通知时间：%s

                """ % (rlt_time, cur_time)
                rlt_send = sm.SendMsg(title, content)
                msg = 'GPS interrupt，send mail waring message.'
                if rlt_send:
                    Log.debug(msg)
                else:
                    Log.debug('GPS interrupt，message ending failed.')
                    while True:
                        Log.debug('Resend mail.')
                        rlt_send = sm.SendMsg(title, content)
                        if rlt_send:
                            Log.debug('Resend success.')
                            break
                return True, msg
            else:
                msg = 'GPS number normal.'
                Log.debug(msg)
                return True, msg
        else:
            msg = 'Database open failure.'
            Log.debug(msg)
            return False, msg
    except Exception as ee:
        Log.debug("Main occur Exception : %s ." % ee.message)
    finally:
        db.close()

if __name__ == '__main__':
    Config = GetConfig()
    FileStat = os.stat(Config)
    ModifyTime = datetime.datetime.fromtimestamp(FileStat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    LastModifyTime = ModifyTime
    print LastModifyTime
    # while True:
    #     try:
    #         rlt, info = Main()
    #         if rlt:
    #             print '检查时间：%s , 检查结果为：%s' % (GetCurStrTime(), info)
    #         else:
    #             print '检查时间：%s，程序发生错误，请查看日志：%s' % (GetCurStrTime(), info)
    #         time.sleep(900)
    #     except Exception as me:
    #         Log.debug('Main occur Exception : %s' % me.message)
    #
