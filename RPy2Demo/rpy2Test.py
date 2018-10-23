__author__ = 'Administrator'



from rpy2.robjects.vectors import DataFrame
from rpy2.robjects.packages import importr,data



r_base=importr('base')
print r_base
faithful_data = DataFrame.from_csvfile('dict.data', sep = " ")
print faithful_data