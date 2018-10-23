#coding:utf-8






from win32com.client import GetObject
WMI = GetObject('winmgmts:')

#List all processes
processes = WMI.InstancesOf('Win32_Process')
for process in processes:
    print process.Properties_('Name')

#Get a specific process
p = WMI.ExecQuery('select * from Win32_Process where Name="chrome.exe"')
#view all possible properties
for prop in p[0].Properties_:
    print prop
#print out PID
print p[0].Properties_('ProcessId').Value