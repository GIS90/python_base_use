# -*- coding: utf-8 -*-

import os
from Util import runLocalCmd
from Log import Log

CURRENT_DIR = os.path.dirname(__file__)
DING_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "DingWarning", "bin"))
assert os.path.exists(DING_DIR)


def sendDingMsg(msg, to="", department=""):
    '''
    通过钉钉接口给指定的人或部门发送钉钉消息
    调用此函数传进的所有参数要求必须是utf-8编码

    :param msg:要通过钉钉发送的信息
    :param to:信息要发送的成员，多个成员之间用|分割，并用双引号将其括起来
    :param department:信息要发送的部门，多个部门之间用|分割，并用双引号将其括起来
    :return:True or False
    '''
    assert isinstance(msg, basestring)
    assert isinstance(to, basestring)
    assert to or department
    oldCwd = os.getcwd()
    cmd = ""
    try:
        os.chdir(DING_DIR)
        if to and department:
            cmd = "java -jar DingWarning.jar -m %s -u %s -p %s" % (msg, to, department)
        elif not to and department:
            cmd = "java -jar DingWarning.jar -m %s -p %s" % (msg, department)
        elif not department and to:
            cmd = "java -jar DingWarning.jar -m %s -u %s " % (msg, to)
        if os.name == 'nt':
            cmd = cmd.decode("utf-8").encode("gbk")
        result, rMsg, stdout, stderr = runLocalCmd(cmd)
        return True, "消息‘%s’成功发送到%s%s" % (msg, to, department) if result else  False, "消息‘%s’失败发送到%s%s" % (msg, to, department)
    except Exception, e:
        Log.error("发送钉钉信息错误，错误信息：" + e.message)
    finally:
        os.chdir(oldCwd)


if __name__ == '__main__':
    sendDingMsg("测试数据", to='包建东')
    print 1
