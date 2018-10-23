# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import codecs
import arcpy
import simplejson

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/5/8"


def toTxt():
    f = open('guoJingJZ.js', 'r').read()
    jsobj = simplejson.loads(f)
    fw = codecs.open('guoJIngPoint.txt', mode='w', encoding='utf-8')
    fw.write('name,x,y\n')
    for key, value in jsobj.iteritems():
        name = key
        x = list(value)[0]
        y = list(value)[1]
        line = "%s, %s, %s" % (name, x, y)
        fw.write(line)
        fw.write('\n')

    print fw.close()


def toJs():
    shape = r"E:\data\jn\guoJing\guoJing_cal.shp"
    fields = ['name', 'x', 'y']
    fw = codecs.open("guoJing_cal.js", 'w', 'utf-8')
    fw.write('var gjall={\n\t')
    n = 1
    size = 1115
    with arcpy.da.SearchCursor(shape, fields) as cursor:
        for row in cursor:
            name = row[0]
            x = row[1]
            y = row[2]
            line = '"%s":["%s","%s"]' % (name, x, y)
            fw.write(line)
            if n != size:
                fw.write(',\n\t')
                n += 1
            else:
                fw.write('\n}')

        print 'end'
        fw.close()


def toguoJjing():

    shape = r"E:\data\jn\guoJing\guoJing_cal.shp"
    fields = ['name']
    size = 0
    names = []
    with arcpy.da.SearchCursor(shape, fields) as cursor:
        for row in cursor:
            name = row[0]
            if name not in names:
                names.append(name)
                size += 1


    fw = codecs.open("guoJing_A-Z_new.js", 'w', 'utf-8')
    fw.write('var gjall=[\n\t')

    fr = open('guoJingA-Z.js', 'r').read()
    jsobj = list(simplejson.loads(fr, encoding='utf8'))
    n = 1
    for line in jsobj:
        line = dict(line)
        name = line['name']
        value = line['value']
        if name in names:
            row = '{"name":"%s","value":"%s"}' % (name, value)
            fw.write(row)
            fw.write(',\n\t') if n != size else fw.write('\n]')
            n += 1

    fw.close()


    print 'end'




toguoJjing()
