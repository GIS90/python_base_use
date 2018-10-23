import os

# path=raw_input()
path = r'E:\temp\shp'
listshp = os.listdir(path)
for i in listshp:
    if i.endswith('.shp') or i.endswith('.shx'):
        print i
