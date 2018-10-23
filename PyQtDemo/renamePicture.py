# -*- coding: utf-8 -*-

import os


def renamePic(filePath):
    if not os.path.exists(filePath):
        return -1
    filenames = os.listdir(filePath)
    print 'Rename Old : %s' % filenames
    for n in xrange(len(filenames)):
        m = n + 1
        oldName = os.path.join(filePath, filenames[n])
        newName = os.path.join(filePath, (str('ct_' + str(m)) + '.jpg'))
        os.renames(oldName, newName)
    return 'Rename Success .'


if __name__ == '__main__':
    filePath = r'E:\data\pic'
    print renamePic(filePath)
