# -*- coding: utf-8 -*-
import unittest
from core.Log import *
from unittest import *


class test_log(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLog(self):
        l = Log.debug("test Log called")

if __name__ == '__main__':
    unittest.main()