# -*- coding: utf-8 -*-

# 定义操作系统的类型，模拟enum


class OSType(object):
    LINUX = 0
    WINDOWS = 1
    OTHER = 2


#定义事件，事件具有类型type与相应的参数，参数为一个tuple,事件是可以序列化的
class Event:
    def __init__(self, type,strs):
        self.type=type
        self.strs=strs
        
    def setType(self,type):
        self.type=type
        
    def getType(self):
        return type
    
    def setStrs(self,strs):
        if isinstance(strs, [].__class__):
            self.strs=strs
        else:
            pass
        
    def getStrs(self):
        return self.strs
    #定义序列化接口，使用一般字符串作为序列化格式
    def getString(self):
        pass
    #反序列化
    def strToThis(self):
        pass


# enum监听的事件类型, 对应的事件分别有对应的参数，目前传的都是一个tuple
class EnumEventType(object):
    # 有效事件监控的开始
    EVENT_START = 0

    # 处理CPU，一般对CPU不敏感，无需监听
    LOCAL_CPU = 1
    REMOTE_CPU = 2

    # 处理内存，一般对内存不敏感，无需监听
    LOCAL_MEMORY = 3
    REMOTE_MEMORY = 4

    # 硬盘，比较敏感，需要监听
    LOCAL_HARD_DISC = 5
    REMOTE_HARD_DISC = 6

    # 进程是否活着，需要监听
    LOCAL_PROCESS_ALIVE = 7
    REMOTE_PROCESS_ALIVE = 8

    # 检查文件是否有更新
    LOCAL_FILE_MODIFIED = 9
    REMOTE_FILE_MODIFIED = 10

    # 到远端的网络是否可达
    REMOTE_TCP_REACHABLE = 11
    REMOTE_UDP_REACHABLE = 12
    REMOTE_ICMP_REACHABLE = 13

    # 监听本地的端口上是否有数据收到
    NO_NEW_SOCKET_DATA_RECV_FOR_TCP = 14
    NO_NEW_SOCKET_DATA_RECV_FOR_UDP = 15

    # 检查数据库里是否有新的数据写入
    DB_TABLE_NO_NEW_DATA = 16
    # 检查数据库的表结构是否被修改了，这个是默认监控的
    DB_TABLE_STRUCTURE_MODIFIED = 17
    # 检查数据库的用户名/密码是否无效了，默认监控的
    DB_INVALID_USER_PASSWORD = 18

    # 检查SSH的账号/密码是否无效，默认监控
    SSH_INVALID_USER_PASSWORD = 19

    # 标记结尾
    EVENT_INVALID = 20
