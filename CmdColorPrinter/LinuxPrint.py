#-*- coding: utf-8 -*-

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
    @staticmethod
    def UseStyle(msg, mode = '', fore = '', back = ''):

        mode  = '%s' % LinuxCMDColorPrint.STYLE['mode'][mode]if LinuxCMDColorPrint.STYLE['mode'].has_key(mode) else ''
        fore  = '%s' % LinuxCMDColorPrint.STYLE['fore'][fore] if LinuxCMDColorPrint.STYLE['fore'].has_key(fore) else ''
        back  = '%s' % LinuxCMDColorPrint.STYLE['back'][back] if LinuxCMDColorPrint.STYLE['back'].has_key(back) else ''
        style = ';'.join([s for s in [mode, fore, back] if s])
        style = '\033[%sm' % style if style else ''
        end   = '\033[%sm' % LinuxCMDColorPrint.STYLE['default']['end'] if style else ''
        print '%s%s%s' % (style, msg, end)

    @staticmethod
    def printRed(msg):
        LinuxCMDColorPrint.UseStyle(msg,fore='red')

if __name__=='__main__':

    print type('测试')
    print type('ceshi')
    LinuxCMDColorPrint.printRed('ceshi')

