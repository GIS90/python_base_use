# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/29'
"""

from Core.DBHand import *
from Core.WtToFile import *
from Core.RltFile import *


def main():
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S%p')
    sql = SQL_CONTENT
    sqlType = SQL_TYPE
    fwName, fwPath = GetRlt()
    fw = os.path.abspath(os.path.join(fwPath, fwName))
    dbH = DBHand()
    dbH.open()
    qr = dbH.query(sqlType, sql)
    data = list(qr)
    rlt = WtToFile(fw, len(data), data)
    print '%s Success .' % now if rlt else '%s Failure .' % now


if __name__ == '__main__':
    main()

