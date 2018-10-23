# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:

    list sort:charu, guibing, kuaisu, maopao, xier, xuanze
    compare the advantages and disadvantages of 6 sort algorithm
------------------------------------------------
"""
import datetime
import time
import random

from decimal import Decimal
from core.dbhandler import *
from core.log import *
from sort.charu import *
from sort.guibing import *
from sort.kuaisu import *
from sort.maopao import *
from sort.xier import *
from sort.xuanze import *

LIST_LEN_MAX = 100 * 100
LIST_EMELENT_MAX = 100 * 100
CAL_NUM = random.randint(1000, 1000)

CUP_TIME = True

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

PRECISION = 8


def sortcomp(l, is_cpu_time=CUP_TIME):
    assert isinstance(l, list)
    assert isinstance(is_cpu_time, bool)

    def __get_cur_time():
        if is_cpu_time:
            return time.clock()
        else:
            return time.time()

    fcprec = "0."
    for i in range(1, PRECISION):
        fcprec += "0"

    charu_startime = __get_cur_time()
    charu(l)
    charu_endtime = __get_cur_time()
    charu_time = charu_endtime - charu_startime
    charu_time = Decimal(charu_time).quantize(Decimal(fcprec))
    infomsg = 'charu sort cost time is %f' % charu_time
    log.info(infomsg)

    guibing_startime = __get_cur_time()
    guibing(l)
    guibing_endtime = __get_cur_time()
    guibing_time = guibing_endtime - guibing_startime
    guibing_time = Decimal(guibing_time).quantize(Decimal(fcprec))
    infomsg = 'guibing sort cost time is %f' % guibing_time
    log.info(infomsg)

    maopao_startime = __get_cur_time()
    maopao(l)
    maopao_endtime = __get_cur_time()
    maopao_time = maopao_endtime - maopao_startime
    maopao_time = Decimal(maopao_time).quantize(Decimal(fcprec))
    infomsg = 'maopao sort cost time is %f' % maopao_time
    log.info(infomsg)

    xier_startime = __get_cur_time()
    xier(l)
    xier_endtime = __get_cur_time()
    xier_time = xier_endtime - xier_startime
    xier_time = Decimal(xier_time).quantize(Decimal(fcprec))
    infomsg = 'xier sort cost time is %f' % xier_time
    log.info(infomsg)

    xuanze_startime = __get_cur_time()
    xuanze(l)
    xuanze_endtime = __get_cur_time()
    xuanze_time = xuanze_endtime - xuanze_startime
    xuanze_time = Decimal(xuanze_time).quantize(Decimal(fcprec))
    infomsg = 'xuanze sort cost time is %f' % xuanze_time
    log.info(infomsg)

    return charu_time, guibing_time, maopao_time, xier_time, xuanze_time


def main():
    host = "localhost"
    port = 3306
    user = "root"
    password = "123456"
    database = "test"
    dbhandle = DBHandler(host=host,
                         port=port,
                         user=user,
                         password=password,
                         database=database)
    dbhandle.open()

    for i in range(1, CAL_NUM + 1):
        now = datetime.datetime.now()
        curtime = now.strftime(TIME_FORMAT)
        l = []
        list_len = random.randint(1, LIST_LEN_MAX)
        infomsg = 'calculate num: %d, list len: %d' % (i, list_len)
        log.info(infomsg)
        print infomsg
        for _ in range(0, list_len):
            l.append(random.randint(1, LIST_EMELENT_MAX))
        charu_time, guibing_time, maopao_time, xier_time, xuanze_time = sortcomp(l)

        insert_sql = "insert into sortcord values('%s', %d, %f, %f, %f, %f, %f);" \
                     % (curtime, list_len, charu_time, guibing_time, maopao_time, xier_time, xuanze_time)
        dbhandle.insert(insert_sql)

    dbhandle.close()


if __name__ == '__main__':
    print 'start run, run sum is %d' % CAL_NUM
    main()
    print 'end run'
