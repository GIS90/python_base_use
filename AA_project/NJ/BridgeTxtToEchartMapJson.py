# -*- coding: utf-8 -*-

import codecs
import os


def TransferJson(txtFile):
    fwDir = os.path.abspath(os.path.basename(txtFile))
    fwName = os.path.splitext(txtFile)[0] + '.js'
    fwPath = os.path.join(fwDir, fwName)
    if os.path.exists(fwPath):
        os.unlink(fwPath)
    fw = codecs.open(fwPath, 'w', 'utf-8')
    fCont = open(txtFile).readlines()
    fNum = 1
    for line in fCont:
        print line
        try:
            fw.write('\t')
            bridge_wast_id = line.split(',')[3]
            bridge_east_id = line.split(',')[4]
            bridge_wast_lon = line.split(',')[5]
            bridge_wast_lat = line.split(',')[6]
            bridge_east_lat = line.split(',')[7]
            bridge_east_lon = line.split(',')[8]
            info_west = '"%s":[%s,%s]' % (bridge_wast_id, bridge_wast_lon, bridge_wast_lat)
            fw.write(info_west)
            fw.write(',')
            fw.write('\r\n')
            fw.write('\t')
            info_east = '"%s":[%s,%s]' % (bridge_east_id, bridge_east_lon, bridge_east_lat)
            fw.write(info_east)
            fw.write(',') if fNum < len(fCont) else 0
            fNum += 1
            fw.write('\r\n')
        except Exception as e:
            print 'occur exception :' + e.message

    fw.close()


if __name__ == '__main__':
    print
    txt = r'E:\data\json\bridge.txt'
    TransferJson(txtFile=txt)
