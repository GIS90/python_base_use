__author__ = 'Administrator'

import sys
import platform as p


print p.python_version()
print p.python_build()
print p.python_revision()
print sys.version
print p.python_branch()
print p.python_implementation()

print p.platform()
print p.platform(aliased=True)
print p.platform(terse=True)
print p.uname()


print p.system()
print p.node()
print p.release()
print p.version()
print p.machine()
print p.processor()