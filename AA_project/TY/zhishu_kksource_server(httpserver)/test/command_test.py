# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/11"

p = "netstat -ano | findstr 80"
command = """
curl -d "{body:{cdbh:12,clsd:40,fxbh:1,hphm:苏E12345,jdz:112.2465641,jgsj:1481784684971,kkmc:太原清远测试卡口,wdz:37.90242936},command:Taiyuan_Demo,protocolType:1}" http://localhost:1990
"""
retcode = COMMAND.execute(command, is_repipe=False)
print retcode






