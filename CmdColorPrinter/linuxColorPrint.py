#-*- coding: utf-8 -*-

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
               'red': 31,  #  红色
               'green': 32,  #  绿色
               'yellow': 33,  #  黄色
               'blue': 34,  #  蓝色
               'purple': 35,  #  紫红色
               'cyan': 36,  #  青蓝色
               'white': 37,  #  白色
               },
        'back':
            {  # 背景
               'black': 40,  # 黑色
               'red': 41,  #  红色
               'green': 42,  #  绿色
               'yellow': 43,  #  黄色
               'blue': 44,  #  蓝色
               'purple': 45,  #  紫红色
               'cyan': 46,  #  青蓝色
               'white': 47,  #  白色
               },
        'mode':
            {  # 显示模式
               'mormal': 0,  # 终端默认设置
               'bold': 1,  #  高亮显示
               'underline': 4,  #  使用下划线
               'blink': 5,  #  闪烁
               'invert': 7,  #  反白显示
               'hide': 8,  #  不可见
               },
        'default':
            {
                'end': 0,
            },
    }
    def UseStyle(msg, mode = '', fore = '', back = ''):

        mode  = '%s' % LinuxCMDColorPrint.STYLE['mode'][mode]if LinuxCMDColorPrint.STYLE['mode'].has_key(mode) else ''
        fore  = '%s' % LinuxCMDColorPrint.STYLE['fore'][fore] if LinuxCMDColorPrint.STYLE['fore'].has_key(fore) else ''
        back  = '%s' % LinuxCMDColorPrint.STYLE['back'][back] if LinuxCMDColorPrint.STYLE['back'].has_key(back) else ''
        style = ';'.join([s for s in [mode, fore, back] if s])
        style = '\033[%sm' % style if style else ''
        end   = '\033[%sm' % LinuxCMDColorPrint.STYLE['default']['end'] if style else ''
        print LinuxCMDColorPrint.STYLE
        print '%s%s%s' % (style, msg, end)

    @staticmethod
    def printRed(msg):
        return LinuxCMDColorPrint.UseStyle(msg,fore='red')
    def printBlack(self,msg):
        return self.UseStyle(msg,fore='black')
    def printGreen(self,msg):
        return self.UseStyle(msg,fore='green')
    def printYellow(self,msg):
        return self.UseStyle(msg,fore='yellow')
    def printBlue(self,msg):
        return self.UseStyle(msg,fore='blue')
    def printPurple(self,msg):
        return self.UseStyle(msg,fore='purple')
    def printCyan(self,msg):
        return self.UseStyle(msg,fore='cyan')
    def printWhite(self,msg):
        return self.UseStyle(msg,fore='white')

if __name__=='__main__':

    print type('测试')
    print type('ceshi')
    LinuxCMDColorPrint.printRed('ceshi')
    LinuxCMDColorPrint.printRed('测试')
    LinuxCMDColorPrint().printBlue('ceshi')
    LinuxCMDColorPrint().printBlue('测试')