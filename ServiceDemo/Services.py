# -*- coding: utf-8 -*-


import win32service
import win32serviceutil
import win32event
import time


class PyService(win32serviceutil.ServiceFramework):
    # 服务信息
    _svc_name_ = "PyService".decode("utf-8")
    _svc_display_name_ = "自定义服务".decode("utf-8")
    _svc_description_ = "Python service demo.".decode("utf-8")

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import os
        f = open('E:\\log.txt', 'w', 0)
        while True:
            fc = os.path.dirname(__name__)
            time.sleep(1)
            info = 'Location time is : ' + time.ctime() + '\r\n'
            f.write(info)
            f.write(fc)
        f.close()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PyService)
