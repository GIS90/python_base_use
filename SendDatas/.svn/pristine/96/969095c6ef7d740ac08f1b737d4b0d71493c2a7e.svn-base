# -*- coding: utf-8 -*-
from Log import Log
import pymssql
import json


class SQLHandler(object):
    URL = ""
    USER = ""
    PASSWORD = ""

    def __init__(self):
        self.conn = None
        self.cur = None

    @classmethod
    def setConnectInfo(cls, url, user, password):
        cls.URL = url
        cls.USER = user
        cls.PASSWORD = password

    def testCheck(self):
        result = self.connect()
        self.close()
        return result

    def connect(self, tryTimes=3, autoConnect=True):
        for i in range(tryTimes):
            self.conn = pymssql.connect(host=SQLHandler.URL,
                                        user=SQLHandler.USER,
                                        password=SQLHandler.PASSWORD,
                                        database="Congest",
                                        timeout="600",
                                        charset="utf8")
            self.cur = self.conn.cursor() if self.conn else None
            if self.conn and self.cur:
                return True
        Log.debug("SQLHandler connect failed")
        return False

    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception:
            pass
        finally:
            self.conn = None
            self.cur = None

    def __del__(self):
        self.close()
        Log.debug("SQLHandler close the session called")

    def queryItems(self, dataType, startTime, endTime):
        msg = "SQLHandler readData " + str(dataType) + " " + str(startTime) + " " + endTime
        Log.debug(msg)
        dataType = int(dataType)
        tableMap = {
            1: self.handleBasicData,
            2: self.handleLink05m,
            3: self.handleMainRoad15m,
            4: self.handleTotal15m,
            5: self.handelPath05m,
            6: self.handleTTIDPI,
            7: self.handleK1Day,
            8: self.handleK2Day,
            9: self.handleK4Day,
        }
        if dataType not in tableMap:
            Log.error("readData dataType not supported " + str(dataType))
            return None, 0
        try:
            return tableMap[dataType](startTime, endTime)
        except Exception, e:
            msg = "readData got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    @staticmethod
    def data2json(data):
        pass

    def handleBasicData(self, startTime, endTime):
        # 1: BasicData
        cmd = "select * from FCD.dbo.BasicData where time BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleBasicData " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                t = (r[0],
                     str(r[1]),
                     r[2],
                     r[3],
                     r[4],
                     r[5])
                objList.append(t)
            if len(objList):
                print "handleBasicData got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["tid",
                                         "time",
                                         "linkid",
                                         "speed",
                                         "length",
                                         "tag"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handleBasicData got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    def handleLink05m(self, startTime, endTime):
        # 2: "FCA.dbo.Link05m",
        cmd = "select * from FCA.dbo.Link05m where time BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleLink05m " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                t = (str(r[0]),
                     r[1],
                     r[2],
                     r[3],
                     r[4],
                     r[5])
                objList.append(t)
            if len(objList):
                print "handleLink05m got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["time",
                                         "linkid",
                                         "speed",
                                         "length",
                                         "sampleNum",
                                         "tag"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handleBasicData got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    def handleMainRoad15m(self, startTime, endTime):
        # 3: "Congest.dbo.MainRoad15m",
        cmd = "select * from Congest.dbo.MainRoad15m where time BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleMainRoad15m " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                t = (r[0],
                     r[1],
                     str(r[2]),
                     r[3],
                     r[4],
                     r[5])
                objList.append(t)
            if len(objList):
                print "handleMainRoad15m got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["roadid",
                                         "class",
                                         "time",
                                         "speed",
                                         "sampleNum",
                                         "IsSysCnt"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handleMainRoad15m got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    def handleTotal15m(self, startTime, endTime):
        # Congest.dbo.Total15m
        cmd = "select * from Congest.dbo.Total15m where time BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleTotal15m " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                c1 = float(r[3]) if r[3] else 0
                c2 = float(r[4]) if r[4] else 0
                c3 = float(r[5]) if r[5] else 0
                c4 = float(r[6]) if r[6] else 0
                c5 = float(r[7]) if r[7] else 0

                g1 = float(r[8]) if r[8] else 0
                g2 = float(r[9]) if r[9] else 0
                g3 = float(r[10]) if r[10] else 0
                g4 = float(r[11]) if r[11] else 0
                g5 = float(r[12]) if r[12] else 0

                speed = float(r[13]) if r[13] else 0
                k3 = float(r[14]) if r[14] else 0
                g5scale = float(r[15]) if r[15] else 0
                IsSystemCount = int(r[16]) if r[16] else 1

                t = (str(r[0]),
                     str(r[1]),
                     str(r[2]),
                     c1,
                     c2,
                     c3,
                     c4,
                     c5,
                     g1,
                     g2,
                     g3,
                     g4,
                     g5,
                     speed,
                     k3,
                     g5scale,
                     IsSystemCount)
                objList.append(t)
            if len(objList):
                print "handleTotal15m got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["time",
                                         "netid",
                                         "class",
                                         "c1",
                                         "c2",
                                         "c3",
                                         "c4",
                                         "c5",
                                         "g1len",
                                         "g2len",
                                         "g3len",
                                         "g4len",
                                         "g5len",
                                         "speed",
                                         "k3",
                                         "g5scale",
                                         "IsSystemCount"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            Log.error("handleTotal15m got exception, error " + str(e))
            return None, 0

    def handelPath05m(self, startTime, endTime):
        # 5: "FCA.dbo.Path05m",
        cmd = "select * from FCA.dbo.Path05m where time BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handelPath05m " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                t = (r[0],
                     str(r[1]),
                     r[2],
                     r[3],
                     r[4])
                objList.append(t)
            if len(objList):
                print "handelPath05m got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["pid",
                                         "time",
                                         "num",
                                         "speed",
                                         "tag"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handelPath05m got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    def handleTTIDPI(self, startTime, endTime):
        # 6: "TTI_DPI",
        cmd = "select * from Congest.dbo.TtiDpiCtmi15m where time BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleK1Day " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                t = (str(r[0]),
                     str(r[1]),
                     str(r[2]),
                     str(r[3]),
                     str(r[4]),
                     str(r[5]))
                objList.append(t)
            jsonObject = {"value": objList,
                          "properties": ["time",
                                         "netid",
                                         "class",
                                         "tti",
                                         "dpi",
                                         "ctmi"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handleK1Day got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    def handleK1Day(self, startTime, endTime):
        # 7: "k1day",
        cmd = "select * from Congest.dbo.K1day where date BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleK1Day " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                t = (r[0],
                     r[1],
                     str(r[2]),
                     r[3],
                     r[4],
                     r[5],
                     r[6],
                     r[7],
                     r[8])
                objList.append(t)
            if len(objList):
                print "handleK1Day got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["netid",
                                         "class",
                                         "date",
                                         "AMK1",
                                         "PMK1",
                                         "k1",
                                         "AMSpd",
                                         "PMSpd",
                                         "Spd"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handleK1Day got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    def handleK2Day(self, startTime, endTime):
        # 8: self.handleK2Day, []
        cmd = "select * from Congest.dbo.K2day where date BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleK2Day " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                # 没有remark字段，没有r[8]
                t = (r[0],
                     r[1],
                     str(r[2]),
                     r[3],
                     r[4],
                     r[5],
                     r[6],
                     r[7],
                     r[9])
                objList.append(t)
            if len(objList):
                print "handleK2Day got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["netid",
                                         "class",
                                         "date",
                                         "c1",
                                         "c2",
                                         "c3",
                                         "c4",
                                         "c5",
                                         "hot"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handleK2Day got exception, error is " + str(e)
            Log.error(msg)
            return None, 0

    def handleK4Day(self, startTime, endTime):
        # 9: self.handleK4Day,
        cmd = "select * from Congest.dbo.K4day where date BETWEEN '" + startTime + "' and '" + endTime + "'"
        cmd = str(cmd)
        Log.debug("handleK4Day " + cmd)
        try:
            self.cur.execute(cmd)
            result = self.cur.fetchall()
            objList = []
            for r in result:
                # 没有remark  r[8]
                t = (str(r[0]),
                     r[1],
                     r[2],
                     r[3],
                     r[4])
                objList.append(t)
            if len(objList):
                print "handleK4Day got {COUNT} items ".format(COUNT=len(objList))
            jsonObject = {"value": objList,
                          "properties": ["date",
                                         "hot",
                                         "linkid",
                                         "runcnt",
                                         "blkcnt"]}
            retVal = json.dumps(jsonObject, sort_keys=True)
            return retVal, len(objList)
        except Exception as e:
            msg = "handleK4Day got exception, error is " + str(e)
            Log.error(msg)
            return None, 0
