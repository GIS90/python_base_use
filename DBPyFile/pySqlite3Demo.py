

import sqlite3

conn=sqlite3.connect('test.db')
print conn
print "Opened Sqlite database successfully"

sql_createtable='''
                    create table test(
                    name    CHAR(20) ,
                    id       INT   NOT  NULL ,
                    age      int ,
                    address  CHAR(50),
                    salary   int
                    )
                '''
# conn.execute(sql_createtable)
# print 'Create Table Successfully !'
sql_insert='''
            insert into test values(
            'A',1,20,'',100)
            '''
# conn.execute(sql_insert)
# conn.commit()
# print 'Insert Table Successfully !'

sql_select='''
            select * from test
            '''
# cursor=conn.execute(sql_select)
# for i in cursor:
#     print i
# print 'Select Table Successfully !'


conn.close()