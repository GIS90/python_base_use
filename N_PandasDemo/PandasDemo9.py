# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from collections import Iterable


from numpy.random import rand
from numpy.random import random_integers


df = pd.DataFrame({'weather': ['cold', 'hot', 'offer', 'cold', 'hot', 'offer'],
                   'food': ['soup', 'bone', 'ice', 'chery', 'ice', 'soup'],
                   'price': 10 * rand(6),
                   'number': random_integers(1, 9, size=(6,))})

# weathers = df.groupby('weather')
# print weathers.first()
# print weathers.last()
# print weathers.mean()

# wf = df.groupby(['weather', 'food'])
# print type(wf.groups)
# print isinstance(wf.groups, Iterable)
# print hasattr(wf.groups, '__iter__')
# for row in wf:
#     print row
#
# print df[2:3].append(df[4:6])


