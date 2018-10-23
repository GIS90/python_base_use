# -*- coding: utf-8 -*-

from Log import Log

def SQLHandle(dataList):
    try:
        assert isinstance(dataList, list)
        sql = 'insert into Services_Status values '
        for data in dataList:
            sql += '('
            for column in data:
                sql += "'%s'," %str(column)
            sql = sql[:-1] + '),'
        return sql[:-1] + ';'
    except Exception, e:
        Log.error('SQL语句拼接错误：' + str(e))