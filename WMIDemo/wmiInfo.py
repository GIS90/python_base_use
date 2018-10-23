# coding:utf-8


import wmi

# 获取远程对象
cObj = wmi.WMI(computer='localhost')
# cObj = wmi.WMI(
#   computer="192.168.2.160",
#   user="administrator",
#   password="0"
# )
print cObj

# 获取内存实使用信息
for Memory in cObj.Win32_PhysicalMemory():
    print "Memory Capacity: %.fMB" % (int(Memory.Capacity) / 1048576)
    print int(cObj.Win32_OperatingSystem()[0].TotalVirtualMemorySize) / 1024
    print int(cObj.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1024
    print int(cObj.Win32_OperatingSystem()[0].FreePhysicalMemory) / 1024
    print int(cObj.Win32_PhysicalMemory()[0].Capacity) / 1024 / 1024

# 获取全部远程对象的进程信息
process = cObj.Win32_Process()
for pro in process:
    print "Id = " + str(pro.ProcessId) + ", Name = " + pro.Name

# 获取指定远程对象的进程信息
process = cObj.Win32_Process(name='ArcSoc.exe')
for pro in process:
    print "Id = " + str(pro.ProcessId) + ", Name = " + pro.Name

# 获取硬盘信息
for disk in cObj.Win32_LogicalDisk(DriveType=3):
    print  "%5s %6.2f%% free" % (disk.Caption, 100.0 * long(disk.FreeSpace) / long(disk.Size))

# 获取服务
stopServices = cObj.Win32_Service(StartMode='Auto', State='Stopped')
if stopServices:
    for stopService in stopServices:
        print '%s Service Is Stopped .' % stopService.Caption
else:
    print 'No Auto Service Stopped .'

# 获取远程计算机系统权限（关机）
cObjRemote = wmi.WMI(computer='127.0.0.1', privileges=["RemoteShutdown"])
os = cObjRemote.Win32_OperatingSystem(Primary=1)[0]
# os.Shutdown()

# 获取启动项
startUpCommands = cObj.Win32_StartupCommand()
for command in startUpCommands:
    print "[%s] %s <%s>" % (command.Location, command.Caption, command.Command)

# 建立站点
# cObjWebService=wmi.WMI(namespace='MicrosoftIISv2')
# for web_server in c.IIsWebService(name='W3Service'):
#     break;
# binding=cObjWebService.new('ServerBinding')
# binding.IP='127.0.0.1'
# binding.Port='8123'
# binding.Hostname='TestServce'
# result,value=web_server.CreateNewSite(
#     PathOfRootVirtualDir=r"c:\inetpub\wwwroot",
#     ServerComment="My Web Site",
#     ServerBindings= [binding.ole_object]
# )
# 获取共享信息
shareInfos = cObj.Win32_Share()
if shareInfos:
    for share in shareInfos:
        print '%s [%s]' % (share.Name, share.Path)

# 获取硬盘格式
DRIVE_TYPES = {
    0: "Unknown",
    1: "No Root Directory",
    2: "Removable Disk",
    3: "Local Disk",
    4: "Network Drive",
    5: "Compact Disc",
    6: "RAM Disk"
}
for drive in cObj.Win32_LogicalDisk():
    print drive.Caption, DRIVE_TYPES[drive.DriveType]
