# coding:utf-8



import MySQLdb
import os
import datetime
import re
import sys
reload(sys)
exec "sys.setdefaultencoding('utf-8')"


def get_conn(host, port, user, pwd, db):
    print 'Connection Information Is :'
    print 'host :', host
    print 'port :', port
    print 'user :', user
    print 'pw :', pwd
    print 'db :', db
    print 'charset :' + 'utf-8'

    try:
        conn = MySQLdb.Connect(host=host,
                               port=port,
                               user=user,
                               passwd=pwd,
                               db=db,
                               charset='utf8')
        return conn if conn else 0
    except Exception as e:
        print "MySQLdb.Connect occur exception: %s" % e.message


def import_db(data_dir, conn):

    if not os.path.exists(data_dir):
        print '%s is not exist, over in advance.' % data_dir
        sys.exit(1)

    global num
    num = 1
    cursor = conn.cursor()
    file_lists = os.listdir(data_dir)
    for file_name in file_lists:
        print '----------%s----------' % file_name
        data_file = os.path.join(data_dir, file_name)
        with open(data_file) as f:
            lines = f.readlines()
            for line in lines:
                reg = '\d'
                pattern = re.compile(reg)
                match = re.match(pattern, line)
                if match:
                    content = line.split('\t')
                    tid = content[3][2:]
                    reg = 'AT\d'
                    pattern = re.compile(reg)
                    match = re.match(pattern, tid)
                    if match:
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
                        print sql_insert
                        try:
                            cursor.execute(sql_insert)
                            conn.commit()
                            print '%d row data insert into gps success !' % num
                            num += 1
                        except Exception as e:
                            print "cursor.execute: %s" % e.message
            print '%s insert into mysql.' % file_name
        cursor.close()
        conn.close()



if __name__ == '__main__':
    print '***************************************'
    print 'Ihe Python Tool Working Data To MySQL !'
    startTime = datetime.datetime.now()
    print '*****Start time :', startTime
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    pwd = '123456'
    db = 'test'
    conn = get_conn(host,
                    port,
                    user,
                    pwd,
                    db)

    DATA_DIR = r'E:\data\ws\data'
    if conn != 0:
        import_db(DATA_DIR, conn)
        print 'Ihe Python Tool Worked OK !'
        endTime = datetime.datetime.now()
        costTime = (endTime - startTime).seconds
        print '*****Cost Time :', costTime
    print '***************************'
