# -*- coding: utf-8 -*-

# 通过此类来收集底层的数据信息，注册成Windows的 Service

import sys
import win32event
import win32service
import win32serviceutil
from Log import Log
sys.path.append("..")
from main import main


class PAMService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PAMService"

    _svc_display_name_ = "PAMService".decode("utf-8")

    _svc_description_ = "PAMService".decode("utf-8")

    def __init__(self, args):
        Log.debug("PAMService __init__ called")
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.runFlag = None

    def SvcDoRun(self):
        self.runFlag = True
        Log.debug("PAMService SvcDoRun")
        while self.runFlag:
            main()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        Log.debug("PAMService svc stop")
        self.runFlag = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)


if __name__=='__main__':
    win32serviceutil.HandleCommandLine(PAMService)