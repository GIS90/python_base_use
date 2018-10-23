# -*- coding: utf-8 -*-

"""
    删除[{'name':'1'},{'name':'6','value':'40954'}]中带有ID=14的元素
    只需要设置修改文件的文件夹，以及生产文件的文件夹即可
    暂时不支持中文，路径请用英文
"""

import os
import re
import codecs


def Del14(Sour, Des):
    assert isinstance(Sour, basestring)
    assert isinstance(Des, basestring)
    if not os.path.exists(Sour):
        return 'Sour is not exist .'
    elif not os.path.isdir(Sour):
        return 'Sour is not dir .'
    elif not os.path.exists(Des):
        return 'Des is not exist .'
    elif not os.path.isdir(Des):
        return 'Des in not Dir'
    JsonList = os.listdir(Sour)
    for js in JsonList:
        jf = os.path.join(Sour, js)
        if os.path.isdir(jf):
            continue
        print jf
        try:
            fw = codecs.open(os.path.join(Des, js), 'w', 'utf-8')
            fContent = open(jf).read()
            JsonContent = fContent.split('=')[1]
            JsonTitle = fContent.split('=')[0]
            print fContent
            fw.write(JsonTitle + '=[')
            for line in JsonContent.split('['):
                reg = "(.*?)'name':'14'(.*?)"
                pattern = re.compile(reg, re.S)
                results = re.search(pattern, line)
                if results is None and line != '':
                    fw.write('[')
                    fw.write(line)
                else:
                    pass
        except Exception as e:
            return 'Occur Exception : ' + e.message
        finally:
            fw.close()
    return 'Python Exccute Success .'


if __name__ == '__main__':
    # 设置需要进行修改的文件夹
    SourcePath = r'E:\data\DelID14Json'
    # 设置新文件存放路径
    DesPath = r'E:\data\Dest'
    print Del14(SourcePath, DesPath)
