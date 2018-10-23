# -*- coding: utf-8 -*-

import win32event
import win32service
import win32serviceutil
import time


class PyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'PythonService'
    _svc_display_name_ = '自定义Python服务'.decode('utf-8')
    _svc_description_ = 'Python Service Demo'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.isAlive = True

    def SvcStop(self):
        # Before we do anything, tell the SCM we are starting the stop process.
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # And set my event.
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        # 把你的程序代码放到这里就OK了
        f = open('d:\\log.txt', 'w', 0)
        f.write(time.ctime(time.time()))
        f.close()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PyService)
