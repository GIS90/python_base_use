# -*- coding: utf-8 -*-

# 这个用于在终端上打印带有颜色的提示信息 方便显示,控制台打印字体支持Windows，Linux

import ctypes
import sys
import platform


def isHostOSWindows():
    sysInfo = platform.architecture()
    return True if sysInfo[1].lower() == "windowspe" else False


def isHostOSLinux():
    sysInfo = platform.architecture()
    return True if sysInfo[1].lower() == "elf" else False

"""
    WindowsCMDColorPrint支持Windows打印，直接调用def即可，暂时只有字体色，后续根据需求可添加背景色+字体色组合
    原理：
        字体颜色定义 ,在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
"""


class WindowsCMDColorPrint(object):
    # 打印类型
    stdInputHandle = -10
    stdOutputHandle = -11
    stdErrorHandle = -12
    # Windows CMD命令行字体颜色定义
    __ForeGroundBLACK = 0x00  # black.
    __ForeGroundDARKBLUE = 0x01  # darkBlue.
    __ForeGroundDARKGREEN = 0x02  # darkGreen.
    __ForeGroundDARKSKYBLUE = 0x03  # darkSkyBlue.
    __ForeGroundDARKRED = 0x04  # darkRed.
    __ForeGroundDARKPINK = 0x05  # darkPink.
    __ForeGroundDARKYELLOW = 0x06  # darkYellow.
    __ForeGroundDARKWHITE = 0x07  # darkWhite.
    __ForeGroundDARKGRAY = 0x08  # darkGray.
    __ForeGroundBLUE = 0x09  # blue.
    __ForeGroundGREEN = 0x0a  # green.
    __ForeGroundSKYBLUE = 0x0b  # skyBlue.F
    __ForeGroundRED = 0x0c  # red.
    __ForeGroundPINK = 0x0d  # pink.
    __ForeGroundYELLOW = 0x0e  # yellow.
    __ForeGroundWHITE = 0x0f  # white.
    # Windows CMD命令行 背景颜色定义 background colors
    __BackGroundDARKBLUE = 0x10  # darkBlue.
    __BackGroundDARKGREEN = 0x20  # darkGreen.
    __BackGroundDARKSKYBLUE = 0x30  # darkSkyBlue.
    __BackGroundDARKRED = 0x40  # darkRed.
    __BackGroundDARKPINK = 0x50  # darkPink.
    __BackGroundDARKYELLOW = 0x60  # darkYellow.
    __BackGroundDARKWHITE = 0x70  # darkWhite.
    __BackGroundDARKGRAY = 0x80  # darkGray.
    __BackGroundBLUE = 0x90  # blue.
    __BackGroundGREEN = 0xa0  # green.
    __BackGroundSKYBLUE = 0xb0  # skyBlue.
    __BackGroundRED = 0xc0  # red.
    __BackGroundPINK = 0xd0  # pink.
    __BackGroundYELLOW = 0xe0  # yellow.
    __BackGroundWHITE = 0xf0  # white.

    stdOutHandle = None

    @staticmethod
    def setCmdColor(color, handle=None):
        if not handle:
            handle = WindowsCMDColorPrint.stdOutHandle
        return ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)

    @staticmethod
    def resetCmdColor():
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundWHITE)

    # 红色
    # red
    @staticmethod
    def printRed(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundRED)
        if not msg.endswith("\n"):
            msg += '\r\n'
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 绿色
    # green
    @staticmethod
    def printGreen(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundGREEN)
        if not msg.endswith("\n"):
            msg += '\r\n'
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗蓝色
    # dark blue
    @staticmethod
    def printDarkBlue(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKBLUE)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗绿色
    # dark green
    @staticmethod
    def printDarkGreen(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKGREEN)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗天蓝色
    # dark sky blue
    @staticmethod
    def printDarkSkyBlue(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKSKYBLUE)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗红色
    # dark red
    @staticmethod
    def printDarkRed(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKRED)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗粉红色
    # dark pink
    @staticmethod
    def printDarkPink(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKPINK)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗黄色
    # dark yellow
    @staticmethod
    def printDarkYellow(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKYELLOW)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗白色
    # dark white
    @staticmethod
    def printDarkWhite(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKWHITE)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 暗灰色
    # dark gray
    @staticmethod
    def printDarkGray(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundDARKGRAY)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 蓝色
    # blue
    @staticmethod
    def printBlue(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundBLUE)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 天蓝色
    # sky blue
    @staticmethod
    def printSkyBlue(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundSKYBLUE)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 粉红色
    # pink
    @staticmethod
    def printPink(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundPINK)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 黄色
    # yellow
    @staticmethod
    def printYellow(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundYELLOW)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()

    # 白色
    # white
    @staticmethod
    def printWhite(msg):
        WindowsCMDColorPrint.setCmdColor(WindowsCMDColorPrint.__ForeGroundWHITE)
        sys.stdout.write(msg)
        WindowsCMDColorPrint.resetCmdColor()


"""
linux的console颜色打印
  格式：\033[显示方式;前景色;背景色m
  说明:

  前景色            背景色            颜色
  ---------------------------------------
    30                40              黑色
    31                41              红色
    32                42              绿色
    33                43              黃色
    34                44              蓝色
    35                45              紫红色
    36                46              青蓝色
    37                47              白色

  显示方式           意义
  -------------------------
     0           终端默认设置
     1             高亮显示
     4            使用下划线
     5              闪烁
     7             反白显示
     8              不可见

  例子：
  \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
  \033[0m          <!--采用终端默认设置，即取消颜色设置-->]]]
"""


class LinuxCMDColorPrint(object):
    STYLE = {
        'fore':
            {  # 前景色
                'black': 30,  # 黑色
                'red': 31,  # 红色
                'green': 32,  # 绿色
                'yellow': 33,  # 黄色
                'blue': 34,  # 蓝色
                'purple': 35,  # 紫红色
                'cyan': 36,  # 青蓝色
                'white': 37,  # 白色
            },
        'back':
            {  # 背景
                'black': 40,  # 黑色
                'red': 41,  # 红色
                'green': 42,  # 绿色
                'yellow': 43,  # 黄色
                'blue': 44,  # 蓝色
                'purple': 45,  # 紫红色
                'cyan': 46,  # 青蓝色
                'white': 47,  # 白色
            },
        'mode':
            {  # 显示模式
                'mormal': 0,  # 终端默认设置
                'bold': 1,  # 高亮显示
                'underline': 4,  # 使用下划线
                'blink': 5,  # 闪烁
                'invert': 7,  # 反白显示
                'hide': 8,  # 不可见
            },
        'default':
            {
                'end': 0,
            },
    }

    @staticmethod
    def UseStyle(msg, mode='', fore='', back=''):
        mode = '%s' % LinuxCMDColorPrint.STYLE['mode'][mode] if LinuxCMDColorPrint.STYLE['mode'].has_key(mode) else ''
        fore = '%s' % LinuxCMDColorPrint.STYLE['fore'][fore] if LinuxCMDColorPrint.STYLE['fore'].has_key(fore) else ''
        back = '%s' % LinuxCMDColorPrint.STYLE['back'][back] if LinuxCMDColorPrint.STYLE['back'].has_key(back) else ''
        style = ';'.join([s for s in [mode, fore, back] if s])
        style = '\033[%sm' % style if style else ''
        end = '\033[%sm' % LinuxCMDColorPrint.STYLE['default']['end'] if style else ''
        print '%s%s%s' % (style, msg, end)

    @staticmethod
    def printRed(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='red')

    @staticmethod
    def printBlack(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='black')

    @staticmethod
    def printGreen(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='green')

    @staticmethod
    def printYellow(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='yellow')

    @staticmethod
    def printBlue(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='blue')

    @staticmethod
    def printPurple(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='purple')

    @staticmethod
    def printCyan(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='cyan')

    @staticmethod
    def printWhite(msg):
        return LinuxCMDColorPrint.UseStyle(msg, fore='white')


def printRed(msg):
    assert isinstance(msg, basestring)
    if isHostOSWindows():
        WindowsCMDColorPrint.printRed(msg)
    elif isHostOSLinux():
        LinuxCMDColorPrint.printRed(msg)
    else:
        pass


def printGreen(msg):
    assert isinstance(msg, basestring)
    if isHostOSWindows():
        setattr(WindowsCMDColorPrint, "stdOutHandle",
                ctypes.windll.kernel32.GetStdHandle(WindowsCMDColorPrint.stdOutputHandle))
        WindowsCMDColorPrint.printGreen(msg)
    elif isHostOSLinux():
        LinuxCMDColorPrint.printGreen(msg)
    else:
        pass


