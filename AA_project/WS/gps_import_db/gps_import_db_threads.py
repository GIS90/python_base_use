# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: gps_import_db.py
@time: 2016/9/22 16:50
@describe: 
@remark: 
------------------------------------------------
"""
import re
import sys
import threading
import time
from Queue import Queue

from core.config import *
from core.dbhandle import *
from core.stmp import *
from core.utils import *


class Producer(threading.Thread):
    def __init__(self, pname, queue, path):
        threading.Thread.__init__(self)
        self.name = pname
        self.__work = queue
        self.__source = path

    def run(self):
        logger.info("%s start run." % self.name)
        file_lists = os.listdir(self.__source)
        if not file_lists:
            logger.error("data_source is not contain data, innormal end")
            sys.exit(1)
        else:
            for fname in file_lists:
                file_file = os.path.abspath(os.path.join(self.__source, fname))
                if os.path.isfile(file_file):
                    print "%s: %s is producing %s to the queue!" % (time.ctime(), self.name, file_file)
                    self.__work.put(file_file)
            print "%s: %s finished." % (datetime.datetime.now(), self.name)


class Consumer(threading.Thread):
    def __init__(self, cname, queue):
        threading.Thread.__init__(self)
        self.name = cname
        self.__work = queue


    def run(self):
        logger.info("%s start run." % self.name)
        db_type, host, port, db, user, pwd = db_config()
        db = DBHandler(db_type, host, port, user, pwd, db)
        db.open()
        row = 1
        while True:
            try:
                data_file = self.__work.get(1, 5)
                print "%s is consuming %s in the queue is consumed!" % (self.name, data_file)
            except Exception as e:
                print "%s finished!" % self.name
                break
            else:
                file_name = os.path.dirname(data_file)
                with open(data_file) as f:
                    lines = f.readlines()
                    for line in lines:
                        if len(line) > 20:
                            content = line.split('\t')
                            tid = content[3][2:]
                            reg_at = 'AT\d'
                            pattern_at = re.compile(reg_at)
                            match_at = re.match(pattern_at, tid)
                            if match_at:
                                tid = int(tid, 36)
                                date = content[0][:4] + "-" + content[0][4:6] + "-" + content[0][6:]
                                hour = content[1][:2] + ":" + content[1][2:4] + ":" + content[1][4:]
                                time = date + " " + hour
                                lon = float(content[4])
                                lat = float(content[5])
                                spd = int(content[6])
                                dir = int(content[7])
                                svc = int(content[8])
                                delays = int(content[9].split("\n")[0])
                                sql_insert = "insert into gps values(%d,'%s',%f,%f,%d, %d, %d, %d)" \
                                             % (tid, time, lon, lat, spd, dir, svc, delays)
                                try:
                                    db.insert(sql_insert)
                                except Exception as e:
                                    print ("run: %s" % e.message)
                                else:
                                    row += 1
                                    if row % 10000 == 0:
                                        print "curreent thread name: %s, row: %d" % (threading.currentThread().getName(), row)
                                        logger.info('%s insert into mysql row: %d' % (file_name, row))
                logger('%s insert into mysql sum: %d row' % (file_name, row))
                db.close()
                f.close()


def report(title, content):
    smtp_host, mailTo_list, mail_user, mail_pw, mail_postfix = stmp_config()
    try:
        sm = SMTPMsg(smtp_host, mailTo_list, mail_user, mail_pw, mail_postfix)
        sm.SendMsg(title, content)
    except Exception as e:
        raise ("report: %s" % e.message)




if __name__ == "__main__":
    start_time = current_time()
    print "%s start run the gps_import_db." % current_stime()
    queue = Queue()
    data_dir = data_config()
    if not os.path.exists(data_dir):
        logger.error("data_source is not exist, innormal end")
        sys.exit(1)

    prod = Producer("producer", queue, data_dir)
    prod.start()
    prod.join()
    for i in range(1, 5, 1):
        consume_name = "consume_" + str(i)
        cons = Consumer(consume_name, queue)
        cons.start()
    end_time = current_time()
    cost_time = cal_time((end_time - start_time).seconds)
    print "gps_import_db: %s" % cost_time
