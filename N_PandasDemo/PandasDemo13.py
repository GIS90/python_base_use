# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

import pandas as pd
import numpy as np
from tempfile import TemporaryFile
from os.path import getsize


np.random.seed(10)
arr = np.random.randn(365, 4)

temf = TemporaryFile(suffix='.xlsx', prefix='test')
df = pd.DataFrame(arr)
print temf.name
df.to_excel(temf.name)

print df.read_excel(temf.name).mean()



# np.savetxt(temf, arr, delimiter=',')
# print getsize(temf.name)
#
# temf = TemporaryFile()
# np.save(temf, arr)
# temf.seek(0)
# loaded = np.load(temf)
# print loaded.shape
# print getsize(temf.name)
#
# df = pd.DataFrame(arr)
# df.to_pickle(temf.name)
# print getsize(temf.name)
# print pd.read_pickle(temf.name)

