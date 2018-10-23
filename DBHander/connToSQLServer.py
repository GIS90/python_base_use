#-*-coding:utf-8-*-




import pyodbc


print "Python Tool Operateing SQL Server DataBase !"
print "Start:--------------------------------------"
print "Test Connection................SQL Server"
connDriver = '{SQL Server}'
connServer = 'localhost'
connDB = 'qd_json'
connUID = 'sa'
connPWD = '123456'
conn = pyodbc.connect(('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                               % (connDriver, connServer, connDB, connUID, connPWD)))
cursor=conn.cursor()
print cursor
print conn
print "Connection Succession"





#select
# sql_select = "select * from population_period_jtqy_copy where data_day='2015-09-07' and period='白天' GROUP BY zqsm"
# sql = "select zqsm from population_period_jtqy_copy where data_day='2015-09-07' GROUP BY zqsm "
#
# print sql
# cursor.execute(sql)
# rs=cursor.fetchall()
# conn.close()
# print rs
# for i in rs:
#       print i
#
#
#
#
# # """
# #insert
# # sql = "select xqsm,sum(resident) from population_period_jtqy where data_day='2015-09-09' and period='早高峰' GROUP BY xqsm"
# # try:
# #       print sql_insert
# #       row=cursor.execute(sql_insert).rowcount
# #       conn.commit()
# #       print row
# #       print "insert success......."
# # except Exception as e:
# #       print "发生错误：",str(e)
# #       conn.rollback()
#
#
# #
# #
# # #delete
# # sql_delete="delete from account where id=1002"
# # try:
# #       print sql_delete
# #       row=cursor.execute(sql_delete).rowcount
# #       print row
# #       conn.commit()
# #       print "delete success......."
# # except Exception as e:
# #       print "发生错误：",str(e)
# #       conn.rollback()
# # """
#
#
# #
# #
# #
# # cursor.close()
# # conn.close()
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
