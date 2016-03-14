#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-08
#Authoruis:     kun/

from core.moudle import Moudle
import sys

"""
终端管理插件支持任何语言与服务(ssh/php/jsp/asp等)
支持linxu命令转换为其他平台命令运行
"""

class terminal(Moudle):

        def __init__():
                print "check init ."

        @staticmethod
        def moudleConsole(self, argv):
                print 'diyConsole !',sys.path[0]
