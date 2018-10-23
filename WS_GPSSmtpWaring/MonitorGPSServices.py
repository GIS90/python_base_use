# -*- coding: utf-8 -*-
"""
 Usage: 'PythonService.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
 Options for 'install' and 'update' commands only:
 --username domain\username : The Username the service is to run under
 --password password : The password for the username
 --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
 --interactive : Allow the service to interact with the desktop.
Options for 'start' and 'stop' commands only:
 --wait seconds: Wait for the service to actually start or stop.
                 If you specify --wait with the 'stop' option, the service
                 and all dependent services will be stopped, each waiting
                 the specified period.
"""

import win32service
import win32serviceutil
import win32event
from main import *


class YunHostServerService(win32serviceutil.ServiceFramework):
    # 服务信息
    _svc_name_ = "Yun Host Server Test".decode("utf-8")
    _svc_display_name_ = "Yun Host Server Test".decode("utf-8")
    _svc_description_ = "Yun Host Server Test.".decode("utf-8")

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        while True:
            Main()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(YunHostServerService)
