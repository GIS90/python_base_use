# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: multi_shape_clip_ogr2ogr.py
@time: 2016/8/12 14:01
@describe:
@remark:
------------------------------------------------
"""


# 导入包
import datetime
import os
import time
import shutil
import sys
import subprocess


def do_clip(input_dir, output_dir, clip_features):
    """
    deal with shape and working to clip
    :param input_dir: input dir
    :param output_dir: output dir
    :param clip_features: clip feature(path + name)
    :return:clip num and failure clip features name
    """

    assert isinstance(input_dir, basestring)
    assert isinstance(output_dir, basestring)
    assert isinstance(clip_features, basestring)
    if not os.path.exists(input_dir) or not os.path.exists(clip_features):
        return 0, []
    if os.path.exists(output_dir):
        print "Output dir is exist, delete."
        shutil.rmtree(output_dir)
        time.sleep(1)
        os.makedirs(output_dir)
    else:
        os.makedirs(output_dir)

    clip_num = 1
    fail_features = []
    list_file = os.listdir(input_dir)
    for input_feature in list_file:
        if str(input_feature).endswith(".shp"):
            input_feature_name = os.path.splitext(input_feature)[0]
            out_features = os.path.join(output_dir, input_feature)
            input_feature = os.path.join(input_dir, input_feature)
            print "Execute clip num = %d, chip feature is: %s" % (clip_num, input_feature_name)
            print out_features, input_feature, clip_features
            try:
                subprocess.call(["ogr2ogr",
                                 "-f",
                                 "ESRI Shapefile",
                                 "-clipsrc",
                                 clip_features,
                                 out_features,
                                 input_feature],
                                shell=True)
                print "Finish."
                clip_num += 1
            except Exception as clip_e:
                fail_features.append(input_feature_name)
                print "%s occur exception is : %s" % (input_feature_name, clip_e.message)
    return clip_num - 1, fail_features


if __name__ == "__main__":

    # 裁剪文件的工作空间，结果文件的存放目录，被裁剪文件路径+名称
    input_dir = r"E:\data\ty\clip"
    output_dir = r"E:\data\ty\data"
    clip_features = r"E:\data\ty\clip\clip.shp"
    start_time = datetime.datetime.now()
    try:
        do_clip(input_dir, output_dir, clip_features)
    except Exception as e:
        print "do_clip occur exception: %s, ahead of the end" % e.message
        sys.exit(1)
    end_time = datetime.datetime.now()
    exe_time = (end_time - start_time).seconds
    print "All features finish and cost time is : %s s." % exe_time
