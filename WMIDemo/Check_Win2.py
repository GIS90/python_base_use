#coding=utf-8

import sys,os,timer,wmi
#import send_mail
from smtplib_email import send_mail
import paramiko
import cmd_color_printers
#reload(sys)
#sys.setdefaultencoding('gbk')
'''
for disk in c.Win32_LogicalDisk ():
	if disk.DriveType == 3:
		space = 100 * long (disk.FreeSpace) / long (disk.Size)
		print "%s has %d%% free" % (disk.Name, space)
'''

class WinCheck(object):
	def __init__(self,c,ipaddress,username,password,memlimit,disklimit,cpulimit,checkprocess=[],checkserver={},status=False,error={},diskover={},runprocess={},stopserver={},display=True):
		self.c = c
		self.ipaddress = ipaddress
		self.username = username
		self.password = password
		self.checkprocess = checkprocess
		self.status = status
		self.error = error
		self.checkserver = checkserver
		self.diskover = diskover
		self.runprocess = runprocess
		self.stopserver = stopserver
		self.memlimit = memlimit
		self.cpulimit = cpulimit
		self.disklimit = disklimit
		self.display = display
	
	def __str__(self):
		showinfo = '''checkprocess = {}
               checkserver = {}
               diskover = {}
               stopserver = {}
               memlimit = {}
               cpulimit = {}
               disklimit = {}
               display = {}
               error = {}'''.format(self.checkprocess,self.checkserver,self.diskover,self.stopserver,self.memlimit,self.cpulimit,self.disklimit,self.display,self.error)
		return showinfo
               #显示并存储磁盘剩余空间
	def Displayfreedisk(self):      
		self.diskover = {}
		for diskinfo in self.c.Win32_LogicalDisk(DriveType=3):
			try:
				self.diskover[diskinfo.Caption] = 100 - int(100.0 * long (diskinfo.FreeSpace) / long (diskinfo.Size))
			except Exception,e:
				temp = str(diskinfo.Caption)+' is not Used!'
				cmd_color_printers.printWhiteRed(str(temp))
				cmd_color_printers.printWhiteBlue(' -> ')
				cmd_color_printers.printWhiteRed(str(e))
				print ''
				continue
			#print self.ipaddress,'->',diskinfo.Caption,self.diskover[diskinfo.Caption],"% used"
 
	#cpu,内存使用率超90%就记录到error字典上
	def CheckSysInfo(self):
		tempip = ''.join(self.ipaddress.split('.')[2:])
		result = 'result'+tempip
		result = {}

		for cpu in self.c.Win32_Processor():
			timestamp = timer.strftime('%a, %d %b %Y %H:%M:%S', timer.localtime())
			result['cpuPercent'] = cpu.loadPercentage

		cs = self.c.Win32_ComputerSystem()
		os = self.c.Win32_OperatingSystem()
		result['memTotal'] = int(int(cs[0].TotalPhysicalMemory)/1024/1024)
		result['memFree'] = int(int(os[0].FreePhysicalMemory)/1024)
		result['memPercent'] = int(((result['memTotal']-result['memFree'])*1.0/result['memTotal'])*100)

		#result.pop('memTotal')
		#result.pop('memFree')
		#print 'result = ',result
		#'''
		for k,v in result.items():
			#print 'k=',k,' v=',v        
			if k in 'cpuPercent':
				if int(v) >= int(self.cpulimit):
					self.error[k] = v
			if k in 'memPercent':
				if int(v) >= int(self.memlimit):
					self.error[k] = v
		#'''
		#self.error[k] = [v for k,v in result.items() if k.lower() in 'cpupercent' and int(v)>=self.cpulimit]
		result = {}

	#显示所有运行的进程
	def Displayallrunning(self):
		for process in self.c.Win32_Process ():
			print self.ipaddress,'=>',process.ProcessId, process.Name

	#显示服务里自动启动，但状态是停止的服务
	def Dispalyautorunbutstop(self):
		stopped_services = self.c.Win32_Service (StartMode="Auto", State="Stopped")
		self.error['checkserver'] = {}
		if stopped_services:
			for s in stopped_services:

				self.stopserver[s.Caption] = 'stop'
				#--------------------------------------------
				if self.display == 'true':
					temp = '\t stopped_services:  %s' % s.Caption
					cmd_color_printers.printYellowBlue(str(temp))
					print ''
				#---------------------------------------------
				if self.error.get('checkserver',0) != 0:

					self.error['checkserver'][s.Caption] = 'stop'
				else:
					self.error['checkserver'] = {}
					self.error['checkserver'][s.Caption] = 'stop'
					break

		else:
			temp = self.ipaddress+' => '+" No auto services stopped"
			cmd_color_printers.printGreenBlue(str(temp))
			print ''
			pass

	#存储服务列表中需要自动启动服务，实际上却没有的！
	def Check_Server(self):
		if len(self.checkserver)>0:
			for cname,cstatus in self.checkserver.items():
				if len(self.stopserver)>0:
					found = False
					for sname,sstatus in self.stopserver.items():
						if str(cname).lower() == str(sname).lower():
							if cstatus == sstatus:
								self.error['checkserver'].pop(str(cname))
								break
							else:
								if self.error.get('checkserver',0) != 0:
									self.error['checkserver'][sname] = sstatus
								else:
									self.error['checkserver'][sname] = sstatus
									break
						else:
							continue
					else:
						if cstatus == 'stop':
							if self.error.get('checkserver',0) != 0:
								temp = cname+' : '+cstatus
								self.error['checkserver'][cname] = cstatus
							else:
								temp = cname+' : '+cstatus
								self.error['checkserver'][cname] = cstatus
				else:
					pass
		else:
			pass

	#往self.error存储错误信息
	def StoreErrorInformation(self):
		pass
	#存储正在运行的进程
	def StortedRunningProcesses(self):
		for process in self.c.Win32_Process():
			if self.runprocess.get('process',0) != 0:
				self.runprocess['process'][process.ProcessId]=process.Name.strip().lower()
			else:
				self.runprocess['process']={}
				self.runprocess['process'][process.ProcessId]=process.Name.strip().lower()

	def DisplayRunningProcesses(self):
		for k,v in self.runprocess.items():
			print k,': ',v
	#检查分区使用情况
	def Check_freedisk(self):
		if self.diskover:
			for tk,tv in self.diskover.items():
				#print tk,tv,self.disklimit
				if int(tv) >= int(self.disklimit):
					if self.error.get('disk',0) != 0:
						keyk = tk.split(':')[0]
						self.error['disk'][keyk] = tv
					else:
						keyk = tk.split(':')[0]
						self.error['disk'] = {}
						self.error['disk'][keyk] = tv

	def Check_runServer(self):
		pass


	#检查存储进程中是否包含要检查的进程
	def Check_processContain(self):
		if len(self.checkprocess)>0:
			for x in self.checkprocess:
				if str(x).startswith('!') and len(str(x))>2:
					self.checkprocess.remove(x)
				# !z 类似这样表示忽略盘符为z的分区的检查
				if str(x).startswith('!') and len(str(x).split('!')[1]) == 1:
					self.checkprocess.remove(x)
					#print 'x--> ',x
					tempdisk = str(x).split('!')[1]+':'
					self.diskover.pop(tempdisk)
		else:
			temp = self.ipaddress+' -> '+' No process to Check... Ignore...'
			cmd_color_printers.printGreenBlue(str(temp))
			print ''
			#pass

		FoundStatus = False
		if len(self.runprocess)>0:
			if self.error.get('process',0) == 0:
				self.error['process'] = []
			else:
				self.error['process'] = []
			for checkprocess in self.checkprocess:
				for id,name in self.runprocess['process'].items():
					if name == checkprocess.strip().lower():
						FoundStatus = True
						break
				if FoundStatus:
					FoundStatus = False
					continue
				else:
					self.error['process'].append(checkprocess.strip())


	def DisplayError(self):
		temp = '\n'
		for k,v in self.error.items():
			temp = k,v
			if v:
				cmd_color_printers.printYellowRed(str(temp))
			else:
				cmd_color_printers.printGreenBlue(str(temp))
			print ''

	def Check_Error(self):
		temp = '\n'
		f = open('checkerrorinfo.txt','a+')
		for k,v in self.error.items():

			if v:
				temp = 'Error:....'+self.ipaddress+' -> '
				cmd_color_printers.printYellowRed(str(temp))
				temp1 =  str(k)+':'+str(v)
				cmd_color_printers.printYellowRed(str(temp1))
				print ''
				thetime = timer.strftime('%Y-%m-%d %H:%M:%S',timer.localtime())
				f.write(str(thetime))
				f.write('..')
				temp2=temp+temp1
				f.write(str(temp2))
				f.write('\n')
				
		f.close()
		self.checkserver = {}
		self.checkprocess = []
		self.error['disk'] = {}
		self.error['checkserver'] = {}
		self.error['checkprocess'] = []

	#开始检查流程
	def StartCheck(self):
		#print 'here is run WinCheck....%s.......' %ipaddress
		#machine = WinCheck(c,ipaddress,username,password,checkprocess=checkprocess,checkserver=checkserver)
		try:
			self.Displayfreedisk()
			#machine.Displayallrunning()
			self.Dispalyautorunbutstop()
			#下面两个执行顺序不能调整
			self.StortedRunningProcesses()
			self.Check_processContain()
			self.Check_freedisk()
			#machine.DisplayRunningProcesses()
			self.Check_Server()
			self.CheckSysInfo()
			#self.DisplayError()
			self.Check_Error()
		except Exception,e:
			f = open('checkerrorinfo.txt','a+')
			thetime = timer.strftime('%Y-%m-%d %H:%M:%S',timer.localtime())
			f.write(str(thetime))
			f.write('..')
			f.write(str(e))
			f.write('\n')
			f.close()

