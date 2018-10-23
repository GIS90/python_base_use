# -*- coding: utf-8 -*-


"""
DBHandler以ORM的方式去操作数据库
remark:
1.暂时只支持 mysql, sqlserver，后续可以健硕
2.功能
open
close
insert_one, insert_many
update_one, update_many
query
"""

from logger import *


class DBTpye(object):
    # 数据库的类型，可扩充
    No = 0
    MYSQL = 1
    SQLSERVER = 2
    ORACLE = 3
    SQLITE = 4
    POSTGRESQL = 5
    MONGDB = 6
    OTHER = 7


class DBHandler(object):
    def __init__(self, dbtype, host, port, user, pwd, db):
        """
        DBHandler 初始化，包含所有数据库的连接内容
        :param dbtype: 数据库类型
        :param host: 主机ip
        :param port: 数据库端口
        :param user: 用户
        :param pwd: 密码
        :param db: 默认数据库名
        :return:
        """
        assert dbtype in range(DBTpye.No, DBTpye.OTHER)
        self.__db_type = dbtype
        self.__host = host
        self.__port = int(port)
        self.__user = user
        self.__pwd = pwd
        self.__db = db
        self.conn = None

    def open(self):
        try:
            return self.__open()
        except Exception as e:
            raise ("DBHandler: open: %s" % e.message)

    def __open(self):
        if self.__db_type == DBTpye.MYSQL:
            import MySQLdb
            self.conn = MySQLdb.connect(host=self.__host,
                                        port=self.__port,
                                        user=self.__user,
                                        passwd=self.__pwd,
                                        db=self.__db)

        elif self.__db_type == DBTpye.SQLSERVER:
            import pyodbc
            DRIVER = '{SQL Server}'
            self.conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                                        % (DRIVER, self.__host, self.__db, self.__user, self.__pwd)))

        elif self.__db_type == DBTpye.ORACLE:
            pass

        elif self.__db_type == DBTpye.SQLITE:
            pass

        elif self.__db_type == DBTpye.POSTGRESQL:
            pass

        elif self.__db_type == DBTpye.MONGDB:
            pass

        else:
            logger.error("DBHandler: open: Not support database type")

        return self.conn

    def close(self):
        try:
            if self.conn is not None:
                self.conn.close()
        except Exception as e:
            raise ("DBHandler: close: %s" % e.message)

    def isopen(self):

        return True if self.conn is not None else False

    def create(self, create_sql):
        assert isinstance(create_sql, basestring)
        pass

    def insert_many(self, insert_sqls):
        assert isinstance(insert_sqls, list)
        for insert_sql in insert_sqls:
            try:
                self.insert(insert_sql)
            except Exception as e:
                raise ("DBHandler: insert_many: %s" % e.message)
        return len(insert_sqls)

    def insert(self, insert_sql):
        assert isinstance(insert_sql, basestring)
        try:
            cursor = self.conn.cursor()
            row = cursor.execute(insert_sql)
            self.conn.commit()
            return row
        except Exception as e:
            self.conn.rollback()
            raise ("DBHandler: insert: %s" % e.message)

    def update_many(self, update_sqls):
        assert isinstance(update_sqls, list)
        for update_sql in insert_sqls:
            try:
                self.update(update_sql)
            except Exception as e:
                raise ("DBHandler: update_many: %s" % e.message)
        return len(insert_sqls)

    def update(self, update_sql):
        assert isinstance(update_sql, basestring)
        try:
            cursor = self.conn.cursor()
            row = cursor.execute(update_sql)
            self.conn.commit()
            return row
        except Exception as e:
            self.conn.rollback()
            raise ("DBHandler: update: %s" % e.message)

    def query(self, query_sql, query_type, times=5):
        """
        进行query查询：
            如果query_type为1，类型字符串，用于查询数据的数量
            如果query_type为2, 返回值列表，用于查询数据的质量
        :param query_sql:进行的sql的查询
        :param query_type: 返回值设定
        :param times: 查询的次数
        :return: 查询结果字符串或者列表
        """
        assert isinstance(query_sql, basestring)
        assert isinstance(query_type, int)
        assert isinstance(times, int)
        assert query_type in (1, 2)
        if self.conn is None:
            for i in range(1, times, 1):
                self.__open()
                if self.conn is not None:
                    break
                if i == times:
                    logger.error('DBHandler: query: open failure')
                    return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query_sql)
            querys = cursor.fetchall()
            if not querys:
                return 0 if query_type == 1 else []
            if query_type == 1:
                return str(querys[0][0])
            else:
                return list(querys)
        except Exception as e:
            raise ('DBHandler: query: %s ' % e.message)
        finally:
            self.close()

    def drop(self, table):
        assert isinstance(table, basestring)
        drop_sql = "drop table if exists %s " % table
        try:
            cursor = self.conn.cursor()
            row = cursor.execute(drop_sql)
            cursor.commit()
            return True if row == 0 else False
        except Exception as e:
            raise ("DBHandler: drop: %s" % e.message)

    def delete_many(self, delete_sql):
        assert isinstance(delete_sql, basestring)
        try:
            cursor = self.conn.cursor()
            row = cursor.execute(delete_sql)
            self.conn.commit()
            return row
        except Exception as e:
            self.conn.rollback()
            raise ("DBHandler: delete_many: %s" % e.message)

    def delete_all(self, table):
        assert isinstance(table, basestring)
        delete_sql = "delete from %s" % table
        try:
            cursor = self.conn.cursor()
            row = cursor.execute(delete_sql)
            self.conn.commit()
            return row
        except Exception as e:
            self.conn.rollback()
            raise ("DBHandler: delete_all: %s" % e.message)
