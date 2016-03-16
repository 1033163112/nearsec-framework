#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-09
#Authoruis:     kun/

import sys
import os


from core import console
from core import pythonstartup 
from utils import fileUtils

def initEnvironment():
	path = '/usr/develop/git/nearsec-framework/moudle/'
	dirPathList = fileUtils.iteratorDir(path)
	sys.path += dirPathList
	print sys.path
		

def start(argv):
	#检测运行环境

	#初始化运行环境
	initEnvironment()

	console.console(argv)

if __name__ == '__main__':
        start(sys.argv)

