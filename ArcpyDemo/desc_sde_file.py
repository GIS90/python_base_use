# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: desc_sde_file.py
@time: 2016/9/1 10:05
@describe: 
@remark: 
------------------------------------------------
"""

import arcpy

desc = arcpy.Describe(r"E:\SQL_SERVER_localhost_sde_target.sde")

# Print workspace properties
#
print "%-24s %s" % ("Connection String:", desc.connectionString)
print "%-24s %s" % ("WorkspaceFactoryProgID:", desc.workspaceFactoryProgID)
print "%-24s %s" % ("Workspace Type:", desc.workspaceType)

# Print Connection properties
#
cp = desc.connectionProperties
print "\nDatabase Connection Properties:"
print "%-12s %s" % ("  Server:", cp.server)
print "%-12s %s" % ("  Instance:", cp.instance)
print "%-12s %s" % ("  Database:", cp.database)
print "%-12s %s" % ("  User:", cp.user)
print "%-12s %s" % ("  Version:", cp.version)

# Print workspace domain names"
#
domains = desc.domains
print "\nDomains:"
for domain in domains:
    print "\t" + domain
