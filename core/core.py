#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-10
#Authoruis:     kun/

import sys
import common
import session

class Core(object):
	
	#确定模块是否存在 存在返回1
	def confirmMoudle(self, path, moudleName):
		for i in range(1, len(path)):
			if moudleName in path[i]:
				if session.PROJECT_ABS_PATH in path[i]: #确定是否为本项目的模块
					return 1

		return 0

		
	def load(self, moudle):
		flag = None
		if self.confirmMoudle(sys.path, moudle):
			obj =  __import__(moudle)
               		cls = getattr(obj, moudle)
               		cls.accpt(cls, moudle)
			flag = 1
				
		if flag is None:
			print "模块不存在！"


	def initParam(self,argv):
		print argv
		
