# -*- coding: utf-8 -*-

# 一些基本操作的封装

from Define import *
import subprocess
import sys
import os
import platform
from datetime import datetime
from Log import Log
import stat
import shutil


def getPythonVersion():
    """获取当前python解释器的版本，默认采用python2.7，如果是python3.*以上的系统可能有兼容性问题
    Args:
        None
    Returns:
        版本的字符串
    Raises:
        None.
    """
    verInfo = sys.version_info
    return str(verInfo.major) + "." + str(verInfo.minor) + "." + str(verInfo.micro)


def getHostOSType():
    """获取当前主机的操作系统类型
    Args:
        None
    Returns:
        定义在Define.py中的OSType
    Raises:
        None.
    """
    sysInfo = platform.architecture()
    retval = OSType.OTHER
    if sysInfo[1].lower() == "windowspe":
        retval = OSType.WINDOWS
    elif sysInfo[1].lower() == "elf":
        retval = OSType.LINUX
    return retval


def getHostOSFullName():
    """获取当前主机的操作系统全称
    Args:
        None
    Returns:
        返回一个字符串，用于描述当前操作系统的类型，需要带上发行版，版本，位数
        如win7_64，字符串需要全部小写
    Raises:
        None.
    """
    sysInfo = {}
    sysVersion = str(platform.platform()).lower()
    sysArchitecture = str(platform.architecture()[0]).lower()
    sysType = str(platform.architecture()[1]).lower()
    sysInfo['type'] = sysType
    sysInfo['architecture'] = sysArchitecture
    sysInfo['version'] = sysVersion

    return sysInfo


def isHostOSWindows():
    """宿主机是否为windows
    Args:
        None
    Returns:
        True or False
    Raises:
        None.
    """
    sysInfo = platform.architecture()
    return True if sysInfo[1].lower() == "windowspe" else False


def isHostOSLinux():
    """宿主机是否为Linux
    Args:
        None
    Returns:
        True or False
    Raises:
        None.
    """
    sysInfo = platform.architecture()
    return True if sysInfo[1].lower() == "elf" else False


def runLocalCmd(cmd, stdoutToPIPE=True, stderrToPIPE=True):
    """执行本地的程序
    Args:
        cmd: 程序名称
        stdoutToPIPE: 输出结果是否打印到stdout
        stderrToPIPE: 输出结果是否打印到stderr
    Returns:
        执行结果的输出，默认包含stdout和stderr的全部内容
    Raises:
        None.
    """
    if not isinstance(stdoutToPIPE, bool) and not isinstance(stderrToPIPE, bool):
        criticalMsg = "runLocalCmd stdoutToPIPE and stderrToPIPE must be boolean value [%s] [%s]" % (stdoutToPIPE, stderrToPIPE)
        return False, criticalMsg, "", ""
    p = None
    if not cmd or not len(cmd):
        warnMsg = "runLocalCmd the command is invalid [%s]" % str(cmd)
        return False, warnMsg, "", ""
    try:
        if stdoutToPIPE and stderrToPIPE:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        elif stdoutToPIPE and not stderrToPIPE:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
        elif not stdoutToPIPE and stderrToPIPE:
            p = subprocess.Popen(cmd, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        elif not stdoutToPIPE and not stderrToPIPE:
            p = subprocess.Popen(cmd, universal_newlines=True, shell=True)
    except Exception, e:
        warnMsg = "runLocalCmd got exception while call subprocess.Popen, error is %s" % str(e)
        return False, warnMsg, "", ""
    else:
        stdoutData, stderrData = p.communicate()
        debugMsg = "runLocalCmd result is [stdout %s] [stderr %s]" % (stdoutData, stderrData)
        return True, debugMsg, stdoutData, stderrData


def removeDir(dirName, recursive=True):
    """删除本地目录
    Args:
        dirName: 目录名称
        recursive: 是否递归删除
    Returns:
        True or False
    Raises:
        None.
    """
    if os.path.exists(dirName) & os.path.isdir(dirName):
        shutil.rmtree(dirName)
        return True
    return False


def removeFile(fileName):
    """删除本地文件
    Args:
        fileName: 文件名称
    Returns:
        True or False
    Raises:
        None.
    """
    if os.path.exists(fileName) & os.path.isfile(fileName):
        os.unlink(fileName)
        return True
    return False


def getCurrentDayTime():
    """获取当前时间的字符串，用于后续一些依赖于时间的操作
    Args:
        None
    Returns:
        当前的时间字符串，比如"2015_12_02"之类的，其中月份和年不足2位的，前面需要用2位补齐
    Raises:
        None
    """
    dt = datetime.now()
    formatterTime = '%Y_%m_%d_%H_%M_%S'
    nowTime = dt.strftime(formatterTime)
    return nowTime


def getCurrentDayInWeek():
    """获取当前天数的星期数目
    Args:
        None
    Returns:
        对应的星期数，比如当前时间为'2015-11-16'，则返回1, 代表周一
    Raises:
        None
    """
    from datetime import datetime
    return datetime.today().isoweekday()


def getStartAndEndTimeOfDate(inputDateTime):
    """获取输入天数的一个tuple, 第一个值为当天的00:00:00, 最后一个值为23:59:59，主要用于SQL的对当天截止时间的操作
    Args:
        字符串，代表时间，类型如"2015-12-3" 和 "2015-12-3 23:56:56"
    Returns:
        tuple数组，如"2015-12-3 00:00:00"和"205-12-3 23:59:59"
    Raises:
        None
    """
    assert isinstance(inputDateTime, basestring)
    return "2015-12-3 00:00:00" "205-12-3 23:59:59"


# TODO
def rename(path):
    import time
    if os.path.exists(path):
        date = time.localtime()
        bakName = os.path.splitext(path)[0]
        for i in range(0, 6):
            if date[i] < 10:
                bakName = bakName + '0' + str(date[i])
            else:
                bakName += str(date[i])
        bakName += os.path.splitext(path)[1]
        os.renames(path, bakName)


def compress(pathName, compressName="", outputFolder=None):
    """
    采用gzip压缩一个文件或者目录，存放的文件名为compressName, 注意，如果是单个文件的话，
    要小量读取，避免读入过大数据造成内存不够
    Args:
        pathName: 文件或目录的名称
        compressName: 压缩后的名称，如果没有指定，则存放在跟PathName一个目录下，名字为Pathname
        的baseName + ".tar.gz", 如pathName为D:\\programes\\tsnav\\fcdb", 为一个目录
        则默认将数据存放在 D:\\programes\\tsnav\\，名称为fcdb.tar.gz里
        outputFolder : 指定的压缩后的输出目录
    Returns:
        True or False
    Raises:
        None
    """
    import gzip
    # os.path.exists(pathName)
    if os.path.isfile(pathName):
        data = None
        if outputFolder:
            path = os.path.join(outputFolder, os.path.split(pathName)[1]) + '.gz'
            path1 = os.path.join(outputFolder, os.path.splitext(os.path.split(pathName)[1])[0]) + '.gz'
        else:
            path = pathName + '.gz'
            path1 = os.path.splitext(pathName)[0] + '.gz'
        rename(path)
        with open(pathName, 'rb') as fIn:
            with gzip.open(path, 'wb') as f:
                while True:
                    data = fIn.read(104857600)
                    if not data:
                        break
                    f.write(data)
                removeFile(pathName)
        if os.path.exists(path):
            if compressName:
                if not outputFolder:
                    outputPath = os.path.join(os.path.split(pathName)[0], os.path.splitext(compressName)[0]) + '.gz'
                else:
                    outputPath = os.path.join(outputFolder, os.path.splitext(compressName)[0]) + '.gz'
                rename(outputPath)
                os.renames(path, outputPath)
            else:
                os.rename(path, path1)
        return True, 'file compression completed'
    elif os.path.isdir(pathName):
        import tarfile
        if outputFolder:
            path = os.path.join(outputFolder, os.path.split(pathName)[1]) + '.gz'
        else:
            path = pathName + '.gz'
        rename(path)
        with tarfile.open(path, 'w:gz') as tar:
            tar.add(pathName)
            removeDir(pathName)
        if os.path.exists(path):
            if compressName:
                if not outputFolder:
                    outputPath = os.path.join(os.path.split(pathName)[0], os.path.splitext(compressName)[0]) + '.gz'
                else:
                    outputPath = os.path.join(outputFolder, os.path.splitext(compressName)[0]) + '.gz'
                rename(outputPath)
                os.renames(path, outputPath)
        return True, 'directory compression completed'
    else:
        return False, 'Path does not exists'


def compressByTarfile(pathName, compressName="", outputFolder=None):
    """
    通过tarfile模块将文件或目录打包压缩，压缩完成后将压缩完的文件或目录删除
    :param pathName: 要压缩的文件或目录的路径
    :param compressName:压缩后的文件名默认使用文件名称加tar.gz
    :param outputFolder:压缩文件的输出目录，默认与压缩的文件同目录
    :return:True or False
    """
    if os.path.exists(pathName):
        import tarfile
        if outputFolder:
            path = os.path.join(outputFolder, os.path.split(pathName)[1]) + '.gz'
        else:
            path = pathName + '.gz'
        rename(path)
        with tarfile.open(path, 'w:gz') as tar:
            tar.add(pathName)
            if os.path.isdir(pathName):
                removeDir(pathName)
            else:
                removeFile(pathName)
        if os.path.exists(path):
            if compressName:
                if not outputFolder:
                    outputPath = os.path.join(os.path.split(pathName)[0], os.path.splitext(compressName)[0]) + '.gz'
                else:
                    outputPath = os.path.join(outputFolder, os.path.splitext(compressName)[0]) + '.gz'
                rename(outputPath)
                os.renames(path, outputPath)
        return True, 'data compression completed'
    else:
        return False, 'Path does not exists'


def getMd5ValueOfPath(pathName, useBinaryMode=True):
    """获取一个目录或文件的md5值, 默认采用MD5的binary模式，如果为False,则采用text模式的MD5
    Args:
        pathName: 文件或目录的名称
        useBinaryMode: 是否采用binaryMode
    Returns:
        对应文件的32字节长度的MD5值
    Raises:
        None
    """
    if not os.path.exists(pathName) or not os.path.isfile(pathName):
        msg = "getMd5ValueOfPath failed, the file doesn't exist or is not a file " + pathName
        Log.debug(msg)
        raise Exception(msg)
    import hashlib
    # The default open mode is text based mode, needs to specify use binary mode
    # In order to avoid the file is too big to cause the OOM, we read 8K data each time
    with open(pathName, 'rb') as fh:
        retVal = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            retVal.update(data)
        return retVal.hexdigest()


def getAllFilesInFolder(dirName):
    """获取一个目录下所有的文件列表，以绝对路径的方式
    Args:
        dirName: 目录名称
    Returns:
        tuple, 第一个值为是否成功，第2个值一个列表，包括该文件夹下所有的文件的绝对路径
    Raises:
        None
    """
    if not os.path.exists(dirName):
        Log.debug("getAllFilesInFolder the path doesn't exist " + dirName)
        return False, []
    if not os.path.isdir(dirName):
        Log.error("getAllFilesInFolder the path is not a directory " + dirName)
        return False, []
    retVal = []
    for dirPath, dirName, allFiles in os.walk(dirName):
        for eachFile in allFiles:
            retVal.append(os.path.abspath(os.path.join(dirPath, eachFile)))
    return True, retVal


def updateTimeWithNTPServer(default, useBackup=False):
    """按照指定的ntpServer地址更新时间
    Args:
        default: 默认的NTP server
        useBackup: 是否采用备用的NTP服务器
    Returns:
        True 如果更新成功 False 失败
    Raises:
        None
    """
    import ntplib
    from time import ctime
    # 作为默认的NTP服务器不可用的备用NTP服务器
    BACKUP_LIST = ['time.asia.apple.com']

    c = ntplib.NTPClient()
    serverList = [default]
    nowTime = datetime.now()
    Log.debug("before NTP sync, time is " + str(nowTime))
    if useBackup and len(BACKUP_LIST):
        serverList.extend(BACKUP_LIST)
    for ntp in serverList:
        try:
            response = c.request(ntp)
        except Exception, e:
            continue
        else:
            timeAfterSync = ctime(response.tx_time)
            Log.debug("after NTP sync, time is " + str(timeAfterSync))
            return True
    Log.warning("updateTimeWithNTPServer failed, time not updated")
    return False

