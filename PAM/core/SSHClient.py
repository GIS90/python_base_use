# -*- coding: utf-8 -*-

# SSH客户端的相关操作和说明
import re
import select
import socket
import time
from datetime import datetime, timedelta

import paramiko

from Log import Log

MAX_BYTES = 32 * 1024


class SSHClient:
    VERSION = '1.0'
    DEFAULT_INTERVAL_TIME = 0.5
    DEFAULT_TIMEOUT = 30

    DEFAULT_EXPECT = '(\#\s*$)|(\>\s*$)|(\?\s*$)|(\)\s*$)|(\:\s*$)|(\$\s*$)'
    DEFAULT_EXPECT += '|(\\$$)'
    DEFAULT_EXPECT += '|(\$\s*$)'

    SSH_SESSION_WIDTH = 1024

    def __init__(self, ip='', username='', password='', port=22):
        """Initialize SSHClient class.

        It will use ssh to connect the remote node.
        Args:
            ip:  the ip address of remote node, '' by default.
            port: ssh port, 22 by default.
            username: ssh user name of remote node, '' by default.
            password: ssh user password of remote node, '' by default.
        Returns:
            None.
        Raises:
            Exception: if given port cannot be converted to integer.
        """
        self.mIP = ip
        try:
            self.mPort = int(port)
        except:
            raise Exception('Invalid port number')
        self.mUser = str(username)
        self.mPassword = str(password)
        self.mSSHClient = None
        self.mPersistentChannel = None
        self.mDefaultDelay = 0.5

    def connect(self):
        """It is used to connect to ssh server and open a interactive shell session.
         Returns:
            None
         Raises:
            Exception: if failed to connect to specified csm.
        """
        Log.debug("SSHClient: connect_to: [ip: %s] [user: %s] [passwd: %s]" % (self.mIP, self.mUser, self.mPassword))
        if self.isConnected():
            self.close()
        return self._open()

    def runShellCmd(self, cmd, expected="", timeout=30):
        """Run the given command via ssh and return the output.

        Args:
            cmd: the shell command to be executed.
            expected: expected string in the output
            timeout: currently not used
        Returns:
            a tuple of boolean and message.
            (True, message) if success
            (False, message) if failure
        Raises:
            None.
        """
        assert isinstance(timeout, int)
        assert timeout >= 5
        if not self.isConnected():
            result, _ = self._open()
            if not result:
                return False, "ssh connect failed"
        output = ''
        deadline = datetime.now() + timedelta(seconds=timeout)
        while datetime.now() < deadline:
            try:
                stdin, stdout, stderr = self.mSSHClient.exec_command(cmd, timeout=timeout)
                # combine stderr with stdout
                # most of the time caller of this method need to analyse the string of stdout or stderr returned by this method, to decide next step.
                # so here, should not raise Exception if stderr is not empty. such as "python -V" may get stderr, but shouldn't raise Exception.
                stdout.channel.set_combine_stderr(True)
                output = stdout.read()
                output = unicode(output, errors='ignore')
            except paramiko.SSHException as err:
                Log.info("execute command fail (%s:%s@%s:%d) commond: %s\nerror message: %s" % (self.mUser,
                                                                                                self.mPassword,
                                                                                                self.mIP,
                                                                                                self.mPort,
                                                                                                cmd,
                                                                                                str(err)))
                if datetime.now() > deadline:
                    return False, str(err)
                else:
                    output = ''
                    continue
            except Exception, err:
                Log.info("read command output fail: %s" % err.message)
                if datetime.now() > deadline:
                    return False, str(err)
                else:
                    output = ''
                    continue
            break

        if expected:
            searcher = ResultSearcher(expected)
            if not searcher.search(output):
                errMsg = 'Did not get expected response:%s in %s seconds msg is %s\n' % (expected, timeout, output)
                return False, errMsg
        output = output.replace("\r\n", "\\n").strip()
        output = output.replace("\\n", "\n").strip()
        return True, output

    def isConnected(self):
        """Check the ssh connection is alive or not
        Returns:
            boolean value stands for the connect state
        Raises:
            None.
        """
        if self.mSSHClient and self.mSSHClient._transport and self.mSSHClient._transport.is_active() and self.mPersistentChannel and not self.mPersistentChannel.closed:
            return True
        else:
            Log.warn("ssh connection lost!")
            return False

    def _open(self):
        """ open the ssh connect state
        Returns:
            a tuple of boolean + errMsg,
            success = True, ""
            failure = False, errMsg
        Raises:
            None.
        """
        Log.debug("SSHClient: open_ssh_connection:%s, %s,%s" % (self, self.mIP, self.mPort))
        self.mSSHClient = None
        self.mPersistentChannel = None

        self.mSSHClient = paramiko.SSHClient()
        self.mSSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.mSSHClient.connect(self.mIP, self.mPort, self.mUser, self.mPassword, timeout=self.DEFAULT_TIMEOUT)
        except paramiko.SSHException, err:
            Log.info('Failed to connect to remote host: %s due to ssh error\n(username: %s / password: %s)%s' % (self.mIP, self.mUser, self.mPassword, str(err)))
            return False, str(err)
        except socket.error, err:
            Log.info('Failed to connect to remote host: %s due to network error\n(username: %s / password: %s) %s' % (self.mIP, self.mUser, self.mPassword, str(err)))
            return False, str(err)
        except Exception, err:
            Log.info("Failed to connect to remote host: %s due to other reason\n(username: %s / password: %s) %s" % (self.mIP, self.mUser, self.mPassword, str(err)))
            return False, str(err)
        self.mSSHClient._transport.set_keepalive(15)
        self.mPersistentChannel = self.mSSHClient.invoke_shell(width=self.__class__.SSH_SESSION_WIDTH)
        time.sleep(self.DEFAULT_INTERVAL_TIME)
        # avoid Infinite loop:
        # it happened in open csm connect with USERID when cli is down
        if not self.isConnected():
            # read buffered data
            if self.mPersistentChannel.recv_ready():
                ret = self.mPersistentChannel.recv(MAX_BYTES)
                Log.warn(ret)
            return False, "open ssh connection failed"
        # Absorb banners
        Log.info("expected endings are:" + self.DEFAULT_EXPECT)
        self.runInteractiveCmd('\r', timeout=5)
        return True, ""

    def close(self):
        """Close the ssh connection.
        """
        if self.mSSHClient and self.mSSHClient._transport and self.mSSHClient._transport.is_active():
            self.mSSHClient.close()
            if self.mPersistentChannel:
                self.mPersistentChannel.close()
        self.mSSHClient = None
        self.mPersistentChannel = None

    def runInteractiveCmd(self, cmd, expected="", timeout=30):
        """run interactive command.
        Args:
            cmd: command to run.
            expected: expected string.
            timeout: timeout of the command
        Returns:
            The output of the command
        Raises:
            Exception: if command is not completed until timeout.
        """
        if not cmd:
            errMsg = "runInteractiveCmd the cmd is empty"
            Log.error(errMsg)
            return False, errMsg

        if not self.isConnected():
            state, _ = self._open()
            if not state:
                return False, "ssh connect failed"

        if not cmd.endswith('\r'):
            cmd += '\r'
        Log.info("runInteractiveCmd the cmd is [" + cmd + "]")
        self.mPersistentChannel.send(cmd)

        output = ''
        deadline = datetime.now() + timedelta(seconds=timeout)
        cntValue = 0
        MAX_NO_NEW_DATA_COUNT = 5
        while datetime.now() <= deadline:
            r, w, e = select.select([self.mPersistentChannel], [], [], self.DEFAULT_INTERVAL_TIME)
            if r:
                ret = self.mPersistentChannel.recv(MAX_BYTES)
                ret = unicode(ret, errors='ignore')
                output += ret
                # we reset the counter until there is really no new data received
                cntValue = 0
                continue
            else:
                cntValue += 1
                # we block to read until there is no new data
                if cntValue == MAX_NO_NEW_DATA_COUNT:
                    break
        searcher = None
        if expected:
            searcher = ResultSearcher(expected)
        else:
            searcher = ResultSearcher(self.DEFAULT_EXPECT)
        if not searcher.search(output):
            errMsg = 'Did not get expected response:%s in %s seconds msg is %s\n' % (expected, timeout, output)
            return False, errMsg
        output = output.replace("\r\n", "\\n").strip()
        output = output.replace("\\n", "\n").strip()
        return True, output

    def __del__(self):
        self.close()

    def startProgramInBackend(self, program, force=True):
        """在后台启动进程，这个需要借助"runuser -l root -c"的方式让程序在后台启动，关闭tty时程序不会自动退出

        Args:
            program 进程名，注意需要使用绝对路径
            force: 如果进程表里已经有同样的进程已经启动，是否强制重新启动
        Returns:
            date string for success or "" for failure
        Raises:
            None
        """
        if not force:
            alive = self.isProgramAlive(program)
            if alive:
                return True
        else:
            cmd = 'runuser -l root -c "{PROGRAM} &"'.format(PROGRAM=program)
            Log.debug("startProgramInBackend [" + cmd + "]")
            result, msg = self.runShellCmd(cmd, timeout=5)
            return result

    def isProgramAlive(self, program):
        """检查进程表里的程序是否为活跃状态
        Args:
            program: 进程名，注意需要使用绝对路径
        Returns:
            True 为存在状
        Raises:
            None
        """
        cmd = "ps -ef|grep '{PROGRAM}'|grep -v grep|wc -l".format(PROGRAM=program)
        state, result = self.runShellCmd(cmd, timeout=5)
        if state:
            try:
                return int(result) >= 1
            except Exception, e:
                Log.debug("isProgramAlive got exception, output is " + result)
                return False
        else:
            return False

    def getMD5OfPath(self, path):
        pass

    def getRemoteTime(self):
        """Get the time string on remote node.

        This keyword will run shell cmd "date" and return the result.
        Args:
            None.
        Returns:
            date string for success or "" for failure
        Raises:
            None.
        """
        if not self.isConnected():
            state, _ = self.connect()
            if not state:
                return ""
        state, dateString = self.runShellCmd("date", timeout=5)
        return dateString if state else ""


class ResultSearcher:
    @staticmethod
    def _escape(arg):
        return re.escape(str(arg)) if arg else ""

    def __init__(self, query):
        self.q = re.compile(query, re.IGNORECASE | re.MULTILINE | re.DOTALL)

    def search(self, buff):
        m = self.q.search(buff)
        if m:
            return m.group()
        else:
            return None
