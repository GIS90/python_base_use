__author__ = 'Administrator'


class PARAS:
    dict = {'population': 'select population,nums from population_hour where data_date="2015-10-05"',
            'resident': 'select resident,nums from population_hour where data_date="2015-10-05"',
            'noworker': 'select noworker,nums from population_hour where data_date="2015-10-05"',
            'workder': 'select workder,nums from population_hour where data_date="2015-10-05"',
            'outlander': 'select outlander,nums from population_hour where data_date="2015-10-05"',
            'passer': 'select passer,nums from population_hour where data_date="2015-10-05"',
            'outlandresident': 'select outlandresident,nums from population_hour where data_date="2015-10-05"',
            'tourist': 'select tourist,nums from population_hour where data_date="2015-10-05"'}


sqlTime = ['2015-09-07', '2015-09-08', '2015-09-09', '2015-09-10', '2015-09-11',
           '2015-09-12', '2015-09-13', '2015-10-04', '2015-10-05']

print sqlTime
for (k, v) in PARAS.dict.items():
    print k + '=' + v

for k in PARAS.dict:
    print "dict[%s] =" % k, PARAS.dict[k]
