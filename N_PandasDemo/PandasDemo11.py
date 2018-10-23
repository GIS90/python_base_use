# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import os
import pandas as pd

os.chdir('E:\data\XY')

cells = pd.read_table('cell_jtxq.txt', header=0, iterator=True)
populations = pd.read_table('population_hour.txt')

flag = True
size = 100 * 100
cell_chunks = []
population_chunks = []

while flag:
    try:
        chunk_cell = cells.get_chunk(size)
        chunk_popul = populations.get_chunk(size)

        cell_chunks.append(chunk_cell)
        population_chunks.append(chunk_popul)
    except StopIteration:
        flag = False
        print 'Iterator is stop'

cell_df = pd.concat(chunk_cell)
popul_df = pd.concat(chunk_popul)

print cell_df.head()
print popul_df.head()


