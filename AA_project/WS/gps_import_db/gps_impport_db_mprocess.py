# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: IportDataMultP.py
@time: 2016/10/26 16:43
@describe: 
@remark: 
------------------------------------------------
"""
import os
import sys
import re
from multiprocessing import Queue
from multiprocessing import Process

from core.config import *
from core.dbhandle import *
from core.stmp import *
from core.utils import *


class Producer(Process):
    def __init__(self, name, data, queue):
        Process.__init__(self)
        self.name = name
        self.data = data
        self.worker = queue

    def run(self):
        assert isinstance(self.data, basestring)

        logger.info("%s is start run." % self.name)
        if not os.path.exists(self.data) or not os.path.isdir(self.data):
            logger.error("Data dir input error, ahead of the end.")
            sys.exit(1)
        data_files = os.listdir(self.data)
        if not data_files:
            logger.error("data_source is not contain data, innormal end")
            sys.exit(1)
        for data_file in data_files:
            data = os.path.abspath(os.path.join(self.data, data_file))
            if os.path.isfile(data):
                self.worker.put(data)
                logger.info("Queue put: %s" % data)
        logger.info("%s is finished produce." % self.name)

    def show(self):
        pass


class Consumer(Process):
    def __init__(self, name, queue):
        Process.__init__(self)
        self.name = name
        self.worker = queue

    def run(self):
        logger.info("%s is start run." % self.name)
        db_type, host, port, db, user, pwd = db_config()
        db = DBHandler(db_type, host, port, user, pwd, db)
        db.open()
        while True:
            try:
                row = 1
                data_file = self.worker.get(1, 20)
                logger.info("Queue get: %s" % data_file)
                if not os.path.exists(data_file):
                    logger.info("%s not in queue" % data_file)
                    continue
            except Exception as e:
                logger.info("%s is finished consume!" % self.name)
                break
            else:
                file_name = os.path.basename(data_file)
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
                                    print ("consume insert: %s" % e.message)
                                else:
                                    row += 1
                                    if row % 1000 == 0:
                                        logger.info('%s insert into mysql row: %d' % (file_name, row))
                    f.close()
                logger.info("%s is finished consume %d via to process %s" % (data_file, row, self.name))
                db.close()


    def show(self):
        pass


if __name__ == "__main__":
    start_time = current_time()
    logger.info("%s start run the gps_import_db." % current_stime())
    queue = Queue()
    data = r"E:\data\ws\data"
    prod = Producer("producer", data, queue)
    prod.start()
    for i in range(1, 5, 1):
        consume_name = "consume_" + str(i)
        cons = Consumer(consume_name, queue)
        cons.start()
    end_time = current_time()
    cost_time = cal_time((end_time - start_time).seconds)
    logger.info("gps_import_db cost time: %s" % cost_time)





