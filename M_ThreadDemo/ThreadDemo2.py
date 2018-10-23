# coding:utf-8
__author__ = 'GIS'

'''
    注：此脚本用来看电影，听音乐，写Python程序共同进行
        模拟电脑cpu多线程技术
'''

import os
import random
import threading


def movie(num):
    m = ['Movie生化危机', 'Movie黑客帝国', 'Movie加勒比海盗', 'Movie速度与激情', 'Movie死亡飞车', 'Movie终极者', 'Movie火影忍者', 'Movie妖精的尾巴']
    for i in range(num):
        print 'Current Run Threading Is %s (%s) , Run Movie >>> %s' % (
            threading.currentThread().name, os.getpid(), random.choice(m))


def music(num):
    m = ['Music不再犹豫', 'Music红日', 'Music最初的梦想', 'Music战斗']
    for i in range(num):
        print 'Current Run Threading Is %s (%s) , Run Music >>> %s' % (
            threading.currentThread().name, os.getpid(), random.choice(m))


def writeThread(num):
    for i in range(num):
        print 'Current Run Threading Is %s (%s) , Run Random >>> %s' % (
            threading.currentThread().name, os.getpid(), random.random())


if __name__ == '__main__':
    ThreadList = []
    movieThread = threading.Thread(target=movie, name='MovieThread', args=(5,))
    musicThread = threading.Thread(target=music, name='MUsicThread', args=(6,))
    writeThread = threading.Thread(target=writeThread, name='WriteThread', args=(4,))
    ThreadList.append(movieThread)
    ThreadList.append(musicThread)
    ThreadList.append(writeThread)
    print 'Current Threading >>> %s' % threading.currentThread().name

    for t in ThreadList:
        t.start()
    print threading.enumerate()
    print threading.activeCount()
