# -*- coding: utf-8 -*-

from SQLHandler import SQLHandler
from Log import Log


def main():
    a = SQLHandler()
    a.setConnectInfo("10.212.129.3", "sa", "#itswork1")
    print a.testCheck()
    a.connect()
    for index in range(1, 10):
        result = a.queryItems(index, "2016-3-8 14:00:00", "2016-3-8 14:05:00")
        if result:
            print "success " + str(index)
            Log.debug(result)
        else:
            print "failure " + str(index)


if __name__ == '__main__':
    main()
