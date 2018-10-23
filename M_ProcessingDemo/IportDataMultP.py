# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: IportDataMultP.py
@time: 2016/10/26 16:43
@describe: 
@remark: 
------------------------------------------------
"""
import os
import sys
from multiprocessing import SimpleQueue
from multiprocessing import Process


class Producer(Process):
    def __init__(self, data, queue):
        Process.__init__(self)
        self.data = data
        self.worker = queue

    def run(self):
        pass

    def produce(self):
        assert isinstance(self.data, basestring)
        assert isinstance(self.worker, SimpleQueue)

        if not os.path.exists(self) or not os.path.isdir(self.data):
            print "Data dir input error, ahead of the end."
            sys.exit(1)

        data_files = os.listdir(self.data)
        for data_file in data_files:
            data = os.path.abspath(os.path.join(self.data, data_file))
            if os.path.isfile(data):
                self.worker.put(data)



    def show(self):
        pass


class Consumer(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.worker = queue

    def run(self):
        pass

    def consum(self):
        pass

    def show(self):
        pass


if __name__ == "__main__":

    queue = SimpleQueue()
    data = r"E:\data\ws\data"
    producer = Producer(data, queue)
    producer.start()




