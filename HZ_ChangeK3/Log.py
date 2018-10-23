# coding:utf-8


import logging
import datetime
import os


def Log(logType, logInfo):
    dt = datetime.datetime.now()
    formatterTime = '%Y-%m-%d-%H-%M-%S%p'
    now = dt.strftime(formatterTime)
    logName = str(now + 'logs.log')
    Curr_Dir = os.path.abspath(os.path.dirname(__file__))
    Log_Dir = os.path.abspath(os.path.join(Curr_Dir, 'logs'))
    if not os.path.exists(Log_Dir):
        os.makedirs(Log_Dir)
    lp = os.path.abspath(os.path.join(Log_Dir, logName))
    # 建立logging对象,设置Logging等级
    Logger = logging.getLogger('Logger')
    Logger.setLevel(logging.DEBUG)
    # 建立文件，将logging信息写入到文件中
    hdl = logging.FileHandler(lp)
    hdl.setLevel(logging.DEBUG)
    # logging的格式
    fmt = logging.Formatter('%(asctime)-5s - %(name)-5s - %(levelname)-5s - %(message)-5s')
    hdl.setFormatter(fmt)
    Logger.addHandler(hdl)
    if logType == 'debug':
        Logger.debug(logInfo)
    elif logType == 'warning':
        Logger.warning(logInfo)
    elif logType == 'error':
        Logger.error(logInfo)
    elif logType == 'critical':
        Logger.critical(logInfo)
    else:
        Logger.info(logInfo)


if __name__ == '__main__':
    Log('warning', 'This is warning')

