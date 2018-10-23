import os

import arcpy

print "start"

# �����������ã����·����Ӣ��Ŀ¼��
inputspace = r"D:\test\02 ���Ÿ�\����0726\shp-2000"  # ����·��
outspace = "D:\\test\\shp"  # ���·��

# ����һ��ִ�д���
x = 0;

# �����������ã�arcpy.SpatialJoin_analysis��Ҫ�����������������������ӱ���

# ���ӱ�������
joinshp = "D:\\test\\join\\��������.shp"

# ��������
arcpy.env.workspace = inputspace
for i in arcpy.ListFiles("*.shp"):
    try:

        arcpy.SpatialJoin_analysis(i, joinshp, os.path.join(outspace, i))

    except Exception as e:

        print(e.message)

    k = os.path.splitext(i)[0]
    print "�ռ����Ӵ���x=", x, "    ", "ִ������Ϊ��", k, "     "
    x = x + 1

print "��������ִ��", x - 1, "��"
print"finish all"

print "---------^ _ ^------------����˧-----------^ _ ^----------"
