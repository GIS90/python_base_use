# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""


import subprocess

child = subprocess.Popen(["ping", "-c", "5", "www.google.com"])
print child.poll()
child.wait()
print("parent process")
