# -*- coding: utf-8 -*-

import win32serviceutil
import win32service
import win32event
from logging.handlers import RotatingFileHandler
import logging
import os
from SocketServer import ThreadingTCPServer
from TCPServer import TCPServer
from Log import Log
from SQLHandler import SQLHandler


class DataSendSVC(win32serviceutil.ServiceFramework):

    _svc_name_ = "DataResendSVC"

    _svc_display_name_ = "DataResendSVC".decode("utf-8")

    _svc_description_ = "DataResendSVC".decode("utf-8")

    def __init__(self, args):
        Log.debug("DataSendSVC __init__ called")
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.server = None

    def SvcDoRun(self):
        Log.debug("DataSendSVC SvcDoRun")
        try:
            self.server = ThreadingTCPServer(("", 6688), TCPServer)
            self.server.allow_reuse_address = True
            self.server.serve_forever()
        except Exception as e:
            msg = "SvcDoRun got exception, error is " + str(e)
            Log.error(msg)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        Log.debug("DataSendSVC svc stop")
        self.server.shutdown()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(DataSendSVC)