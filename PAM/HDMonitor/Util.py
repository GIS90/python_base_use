# -*- coding: utf-8 -*-

import os
import shutil


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


def removePath(path, recursive=True):
    try:
        if not os.path.exists(path):
            return True
        if os.path.isdir(path):
            return removeDir(path)
        elif os.path.isfile(path):
            return removeFile(path)
    except Exception, e:
        return False