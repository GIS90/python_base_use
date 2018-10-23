# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
itertools 的使用
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/27"


from itertools import combinations


def solve(lst, upperbound):
    candidates = []
    for n in lst:
        for count in range(upperbound//n):
            candidates.append(n)
    allcomb = set()
    for l in range(1, len(candidates)+1):
        for comb in combinations(candidates, l):
            if not comb in allcomb:
                allcomb.add(comb)
                if sum(comb) <= upperbound:
                    print('+'.join([str(n)for n in comb]))

solve([1,2,3], 10)





