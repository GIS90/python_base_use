# coding:utf-8

import codecs
import datetime
import os
import sys

import arcpy

GDAL_DRIVER = "ESRI ShapeFile"
FIELDS = ["OBJECTID_1", "SHAPE@JSON"]
JS_FILE_NUM = 24


class LineToJson(object):
    def __init__(self, shape, fields):
        assert isinstance(shape, basestring)
        assert isinstance(fields, list)
        self.shape = shape
        self.fields = fields

    def count(self):
        """
        get shape feature count
        :return:
        """
        assert isinstance(self.shape, basestring)
        if not os.path.isfile(self.shape):
            return 0
        try:
            from osgeo import ogr
        except ImportError:
            import ogr
        driver = ogr.GetDriverByName(GDAL_DRIVER)
        ds = driver.Open(self.shape, 0)
        return 0 if ds is None else ds.GetLayer().GetFeatureCount()
        # if ds in None:
        #     return 0
        # layer = ds.GetLayer()
        # count = layer.GetFeatureCount()
        # return count

    def transform(self, line_num, output_dir):
        assert isinstance(output_dir, basestring)
        assert isinstance(line_num, int)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        shape_file = os.path.basename(self.shape)
        shape_dir = os.path.abspath(os.path.dirname(self.shape))
        arcpy.env.workspace = shape_dir
        count = js_num = 0
        shape_num = self.count()
        print "%s is executed." % shape_file
        with arcpy.da.SearchCursor(self.shape, self.fields) as cursor:
            for row in cursor:
                if count % line_num == 0:
                    js_num += 1
                    js = os.path.abspath(os.path.join(output_dir, ("data7_" + str(js_num) + ".js")))
                    print "--------%s is working." % js
                    if os.path.exists(js):
                        os.unlink(js)
                    js_fw = codecs.open(js, mode="w", encoding="utf8")
                    js_fw.write("{")
                objectid = int(row[0])
                geomtry = str(row[1]).split(':[[[')[1].split(']]],"')[0]
                geo_s_1 = geomtry.split(']],[[')
                geo_new = '[[['
                for g in range(0, len(geo_s_1)):
                    geo_s_2 = geo_s_1[g].split('],[')
                    for i in range(0, len(geo_s_2)):
                        i_new = geo_s_2[i].split(',')
                        for ii in range(0, len(i_new)):
                            value = str(float(i_new[ii]))
                            geo_new += value
                            if ii == 0:
                                geo_new += ','
                        if i < len(geo_s_2) - 1:
                            geo_new += '],['
                    if g < len(geo_s_1) - 1:
                        geo_new += '],['
                geo_new += ']]]'
                line = '"' + str(objectid) + '": ' + geo_new
                js_fw.write(line)
                if (count + 1) % line_num == 0 or (count + 1) == shape_num:
                    js_fw.write("}")
                    js_fw.close()
                else:
                    js_fw.write(",")
                count += 1



if __name__ == '__main__':
    print 'It python tool start working !'
    start_time = datetime.datetime.now()
    input_source = r'E:\data\wz\Linkgeo_new'
    if not os.path.exists(input_source):
        print "%s is not exist, ahead of the end." % input_source
    elif not os.path.isdir(input_source):
        print "%s is not folder, ahead of the end." % input_source
    else:
        arcpy.env.workspace = input_source
        for shp in arcpy.ListFiles("*.shp"):
            shape = os.path.abspath(os.path.join(input_source, shp))
            output_source = os.path.abspath(os.path.join(input_source, (os.path.splitext(shp)[0] + "_js")))
            lj = LineToJson(shape, FIELDS)
            js_line_num = lj.count() / JS_FILE_NUM + 1
            lj.transform(js_line_num, output_source)
    end_time = datetime.datetime.now()
    cost_time = (end_time - start_time).seconds
    print 'Cost time : %s s.' % cost_time
