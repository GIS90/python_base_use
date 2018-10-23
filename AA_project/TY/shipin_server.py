# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
it is use to generate ShiPin js file
that taiyuan project of Kakou traffic big data platfrom
data source from to txt format data, via deal with data,
finally import to mysql database

use:
set mysql config
python shipin_server.py

------------------------------------------------
"""
import codecs
import sys
import os
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')


conn = MySQLdb.connect(host='127.0.0.1',
                       user='root',
                       passwd='123456',
                       db='ty',
                       port=3306,
                       connect_timeout=5,
                       charset="utf8")
cursor = conn.cursor()

camtypes = {
    'qj': "球机",       # 球机
    'sj': "事件检测"    # 事件检测
}
'15301068287'


jspath = r"E:\data\ty\shipin"
if not os.path.exists(jspath):
    os.makedirs(jspath)
jsfile = os.path.join(jspath, 'shipin.js')
fw = codecs.open(jsfile, mode="w", encoding="utf8", errors="strict", buffering=1)
fw.write("[\n\t")

index = 0
for key, value in camtypes.iteritems():
    fw.write('{"name": "%s",' % key)
    sql = 'select cid, x, y, cname from shipin_online where ctype = "%s"; ' % value
    print sql
    cursor.execute(sql)
    rows = cursor.fetchall()
    count = len(rows)
    n = 1
    fw.write('"value": [')
    for row in rows:
        #print row
        cid = str(row[0]).strip()
        lon = row[1]
        lat = row[2]
        addr = row[3].encode('utf8').strip()
        addr = addr.replace("\n", "")

        if 112 < lon < 113 and 37 < lat < 38 and cid and addr:
            line = '{"id": "%s", "lon": %s, "lat": %s, "addr": "%s"}' % (cid, lon, lat, addr)
            # print line
            fw.write(line)
            fw.write(",") if n < count else 0
        n += 1
        print n
    index += 1
    fw.write(']},\n\t') if index < 2 else fw.write(']}\n]')


fw.close()
print "end"
