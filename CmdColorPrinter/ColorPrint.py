# coding:utf-8

import ctypes, sys

# 说明：
#    控制台颜色打印分别是Windows与Linux
#    直接调用相对应的类，调用方法即可


# Windows的console的颜色打印
stdInputHandle = -10
stdOutputHandle = -11
stdErrorHandle = -12

# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
# 由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中

# Windows CMD命令行字体颜色定义
FOREGROUND_BLACK = 0x00  # black.
FOREGROUND_DARKBLUE = 0x01  # dark blue.
FOREGROUND_DARKGREEN = 0x02  # dark green.
FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
FOREGROUND_DARKRED = 0x04  # dark red.
FOREGROUND_DARKPINK = 0x05  # dark pink.
FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
FOREGROUND_DARKWHITE = 0x07  # dark white.
FOREGROUND_DARKGRAY = 0x08  # dark gray.
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_SKYBLUE = 0x0b  # skyblue.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_PINK = 0x0d  # pink.
FOREGROUND_YELLOW = 0x0e  # yellow.
FOREGROUND_WHITE = 0x0f  # white.
# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_DARKBLUE = 0x10  # dark blue.
BACKGROUND_DARKGREEN = 0x20  # dark green.
BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
BACKGROUND_DARKRED = 0x40  # dark red.
BACKGROUND_DARKPINK = 0x50  # dark pink.
BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
BACKGROUND_DARKWHITE = 0x70  # dark white.
BACKGROUND_DARKGRAY = 0x80  # dark gray.
BACKGROUND_BLUE = 0x90  # blue.
BACKGROUND_GREEN = 0xa0  # green.
BACKGROUND_SKYBLUE = 0xb0  # skyblue.
BACKGROUND_RED = 0xc0  # red.
BACKGROUND_PINK = 0xd0  # pink.
BACKGROUND_YELLOW = 0xe0  # yellow.
BACKGROUND_WHITE = 0xf0  # white.


class CMDColorPrint():
    stdOutHandle = ctypes.windll.kernel32.GetStdHandle(stdOutputHandle)

    def setCmdColor(self, color, handle=stdOutHandle):
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool

    def resetCmdColor(self):
        self.setCmdColor(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

    # 暗蓝色
    # dark blue
    def printDarkBlue(self, mess):
        self.setCmdColor(FOREGROUND_DARKBLUE)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 暗绿色
    # dark green
    def printDarkGreen(self, mess):
        self.setCmdColor(FOREGROUND_DARKGREEN)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 暗天蓝色
    # dark sky blue
    def printDarkSkyBlue(self, mess):
        self.setCmdColor(FOREGROUND_DARKSKYBLUE)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 暗红色
    # dark red
    def printDarkRed(self, mess):
        self.setCmdColor(FOREGROUND_DARKRED)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 暗粉红色
    # dark pink
    def printDarkPink(self, mess):
        self.setCmdColor(FOREGROUND_DARKPINK)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 暗黄色
    # dark yellow
    def printDarkYellow(self, mess):
        self.setCmdColor(FOREGROUND_DARKYELLOW)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 暗白色
    # dark white
    def printDarkWhite(self, mess):
        self.setCmdColor(FOREGROUND_DARKWHITE)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 暗灰色
    # dark gray
    def printDarkGray(self, mess):
        self.setCmdColor(FOREGROUND_DARKGRAY)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 蓝色
    # blue
    def printBlue(self, mess):
        self.setCmdColor(FOREGROUND_BLUE)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 绿色
    # green
    def printGreen(self, mess):
        self.setCmdColor(FOREGROUND_GREEN)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 天蓝色
    # sky blue
    def printSkyBlue(self, mess):
        self.setCmdColor(FOREGROUND_SKYBLUE)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 红色
    # red
    def printRed(self, mess):
        self.setCmdColor(FOREGROUND_RED)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 粉红色
    # pink
    def printPink(self, mess):
        self.setCmdColor(FOREGROUND_PINK)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 黄色
    # yellow
    def printYellow(self, mess):
        self.setCmdColor(FOREGROUND_YELLOW)
        sys.stdout.write(mess)
        self.resetCmdColor()

    # 白色
    # white
    def printWhite(self, mess):
        self.setCmdColor(FOREGROUND_WHITE)
        sys.stdout.write(mess)
        self.resetCmdColor()


# linux的console颜色打印
#   格式：\033[显示方式;前景色;背景色m
#   说明:
#
#   前景色            背景色            颜色
#   ---------------------------------------
#     30                40              黑色
#     31                41              红色
#     32                42              绿色
#     33                43              黃色
#     34                44              蓝色
#     35                45              紫红色
#     36                46              青蓝色
#     37                47              白色
#
#   显示方式           意义
#   -------------------------
#      0           终端默认设置
#      1             高亮显示
#      4            使用下划线
#      5              闪烁
#      7             反白显示
#      8              不可见
#
#   例子：
#   \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
#   \033[0m          <!--采用终端默认设置，即取消颜色设置-->]]]

class LinuxCMDColorPrint():
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

    def UseStyle(self, msg, mode='', fore='', back=''):
        mode = '%s' % self.STYLE['mode'][mode] if self.STYLE['mode'].has_key(mode) else ''
        fore = '%s' % self.STYLE['fore'][fore] if self.STYLE['fore'].has_key(fore) else ''
        back = '%s' % self.STYLE['back'][back] if self.STYLE['back'].has_key(back) else ''
        style = ';'.join([s for s in [mode, fore, back] if s])
        style = '\033[%sm' % style if style else ''
        end = '\033[%sm' % self.STYLE['default']['end'] if style else ''
        return '%s%s%s' % (style, msg, end)

    def printRed(self, msg):
        return self.UseStyle(msg, fore='red')

    def printBlack(self, msg):
        return self.UseStyle(msg, fore='black')

    def printGreen(self, msg):
        return self.UseStyle(msg, fore='green')

    def printYellow(self, msg):
        return self.UseStyle(msg, fore='yellow')

    def printBlue(self, msg):
        return self.UseStyle(msg, fore='blue')

    def printPurple(self, msg):
        return self.UseStyle(msg, fore='purple')

    def printCyan(self, msg):
        return self.UseStyle(msg, fore='cyan')

    def printWhite(self, msg):
        return self.UseStyle(msg, fore='white')
