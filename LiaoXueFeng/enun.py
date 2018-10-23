# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from enum import Enum, unique


@unique
class Animals(Enum):
    ant = 1
    dog = 1
    cat = 3


print Animals
