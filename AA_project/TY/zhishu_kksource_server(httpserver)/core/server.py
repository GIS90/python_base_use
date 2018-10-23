# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
http server use to accept
------------------------------------------------
"""
import datetime
import json
from cgi import parse_header, parse_multipart
from sys import version as python_version

from config import *
from dbhandler import *
from log import *

reload(sys)
sys.setdefaultencoding("utf8")

if python_version.startswith("3"):
    from http.server import BaseHTTPRequestHandler
else:
    from BaseHTTPServer import BaseHTTPRequestHandler

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/9"

FORMMAT = "%Y-%m-%d %H:%M:%S"

_db_host, _db_port, _db_user, _db_password, _db_database = get_db_config()
kakou_table = get_kakou_table_config()
kakou_folder = get_kakou_folder_config()
try:
    dbhandle = DBHandler(host=_db_host,
                         port=_db_port,
                         user=_db_user,
                         password=_db_password,
                         database=_db_database)
    dbhandle.open()
    log.info("KaKouRequestHandler dbhandler is open")
except Exception as e:
    emsg = "KaKouRequestHandler dbhandler open is error: %s" % e.message
    log.error(emsg)
    sys.exit()


class KaKouRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print "Get method request"
        pass

    def do_POST(self):
        ctype, pdict = parse_header(self.headers.getheader("content-type"))
        if ctype == "multipart/form-data":
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == "application/x-www-form-urlencoded":
            request_size = int(self.headers["content-length"])
            # postvars = parse_qs(self.rfile.read(request_size), keep_blank_values=1)  # dict type data stream
            postvars = str(self.rfile.read(request_size))  # str type data stream
        else:
            postvars = ""
        if postvars is None:
            pass

        value = KaKouRequestHandler.kakou_parse(postvars)
        try:

            insert_values = "insert into %s values %s;" % (kakou_table, value)
            print insert_values
            dbhandle.insert(insert_values)
        except Exception as e:
            emsg = "KaKouRequestHandler kakou data is error: %s" % e.message
            log.error(emsg)

    @staticmethod
    def kakou_parse(postvars):
        assert isinstance(postvars, basestring)

        def get_tid(hphm):
            assert isinstance(hphm, basestring)

            carbrand = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
                        '9': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', ' 16': 'G', '17': 'H',
                        '18': 'I', '19': 'J', '20': 'K', ' 21': 'L', '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q',
                        '27': 'R', '28': 'S', '29': 'T', '30': 'U', '31': 'V', '32': 'W', '33': 'X', '34': 'Y', '35': 'Z'
                        , '36': '晋'
                        , '37': '粤'
                        , '38': '浙'
                        , '39': '京'
                        , '40': '沪'
                        , '41': '川'
                        , '42': '津'
                        , '43': '渝'
                        , '44': '鄂'
                        , '45': '赣'
                        , '46': '冀'
                        , '47': '蒙'
                        , '48': '鲁'
                        , '49': '苏'
                        , '50': '辽'
                        , '51': '吉'
                        , '52': '皖'
                        , '53': '湘'
                        , '54': '黑'
                        , '55': '琼'
                        , '56': '贵'
                        , '57': '桂'
                        , '58': '云'
                        , '59': '藏'
                        , '60': '陕'
                        , '61': '甘'
                        , '62': '宁'
                        , '63': '青'
                        , '64': '豫'
                        , '65': '闽'
                        , '66': '新'
                        }
            print carbrand
            for i in hphm:
                for key, value in carbrand.items():
                    if i == value:
                        hphm = hphm.replace(i, str(key))
            return hphm

        postvars = postvars.decode('gbk').encode('utf8')
        postvars = """
{       "body":{"cdbh":"12","clsd":"40","fxbh":"1","hphm":"苏EFA345",
"jdz":"112.2465641","jgsj":1481784684971,"kkmc":"太原清远测试卡口","wdz":"37.90242936"},
"command":"Taiyuan_Demo","protocolType":"1"}
        """
        kakou = json.loads(postvars)

        hphm = kakou['body']['hphm']
        tid = get_tid(hphm)
        jgsj = kakou['body']['jgsj']
        kkmc = kakou['body']['kkmc']
        clsd = kakou['body']['clsd']
        dateArray = datetime.datetime.utcfromtimestamp(jgsj / 1000)
        jgsj = dateArray.strftime(FORMMAT)
        fxbh = kakou['body']['fxbh']
        svc = str(1)
        delay = str(0)

        value = "('" + tid + "','" + jgsj + "','" + kkmc + "'," + clsd + "," + fxbh + "," + svc + "," + delay + ")"
        return value



        # hphm = kakou.split("hphm:")[1].split(",")[0].decode("gbk").encode("utf-8")
        # jgsj = int(kakou.split("jgsj:")[1].split(",")[0])
        # kkmc = kakou.split("kkmc:")[1].split(",")[0].decode("gbk").encode("utf-8")
        # clsd = kakou.split("clsd:")[1].split(",")[0]
        # # cdbh = kakou.split("cdbh:")[1].split(",")[0]
        # # fxbh = kakou.split("fxbh:")[1].split(",")[0]
        # # jdz = kakou.split("jdz:")[1].split(",")[0]
        # # wdz = kakou.split("wdz:")[1].split("}")[0]
        # dateArray = datetime.datetime.utcfromtimestamp(jgsj / 1000)
        # jgsj = dateArray.strftime(FORMMAT)
        # dir = "1"
        # svc = "1"
        # delay = "0"
        # # value = "('" + hphm + "','" + jgsj + "'," + cdbh + "," + fxbh + "," + clsd + ",'" + kkmc + "'," + jdz + "," + wdz + ")"
        # value = "('" + hphm + "','" + jgsj + "','" + kkmc + "'," + clsd + "," + dir + "," + svc + "," + delay + ")"
        # return value
