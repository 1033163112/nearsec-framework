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
from core import session

def initEnvironment():
	session.PROJECT_ABS_PATH = sys.path[0] + '/moudle/'
	dirPathList = fileUtils.iteratorDir(session.PROJECT_ABS_PATH)
	sys.path += dirPathList
		

def start(argv):
	#检测运行环境

	#初始化运行环境
	initEnvironment()

	console.console(argv)

if __name__ == '__main__':
        start(sys.argv)

