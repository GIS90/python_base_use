# -*- coding: utf-8 -*-


import logging
import datetime
import os


def log(logType, logInfo):
    dt = datetime.datetime.now()
    formatterTime = '%Y-%m-%d-%H-%M-%S%p'
    now = dt.strftime(formatterTime)
    print '%s Ouucr Exception !' % now

    fileName = str(now)
    filePath = os.path.join(os.getcwd(), 'log')
    if os.path.exists(filePath):
        pass
    else:
        os.makedirs(filePath)

    # 建立logging对象,设置Logg等级
    Logg = logging.getLogger('LoggInfo')
    Logg.setLevel(logging.DEBUG)

    # 建立文件，将logging信息写入到文件中
    LoggName = fileName + 'LogInfo.log'
    LoggFile = os.path.join(filePath, LoggName)
    hdlr = logging.FileHandler(LoggFile)
    hdlr.setLevel(logging.DEBUG)

    # 将日志信息打印到控制台
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    # logging的格式
    formatter = logging.Formatter('%(asctime)-5s - %(name)-5s - %(levelname)-5s - %(message)-5s')
    hdlr.setFormatter(formatter)

    Logg.addHandler(hdlr)
    Logg.addHandler(sh)

    if (logType.islower() == 'debug'):
        Logg.debug(logInfo)
    elif (logType.islower() == 'warning'):
        Logg.warning(logInfo)
    elif (logType.islower() == 'error'):
        Logg.error(logInfo)
    elif (logType.islower() == 'critical'):
        Logg.critical(logInfo)
    else:
        Logg.info(logInfo)


if __name__ == '__main__':
    log('error', 'This is Error')
