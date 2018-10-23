#-*-coding:utf-8-*-



import connToSQLServer




print "Python Tool Operateing SQL Server DataBase !"
print "Start:--------------------------------------"



print "Test Connection................SQL Server"

conn= connToSQLServer.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=sde;UID=sa;PWD=123456")
cursor=conn.cursor()


print "Connection Succession"



#dbName=raw_input("���������ݿ����ƣ�")
db_del_sql="drop database test"

try:
    cursor.execute(db_del_sql)
    conn.commit()
    print "Delete DataBase Success............"
except Exception as e:
    conn.rollback()
    print e.message
    print "Delete DataBase Failure............"
