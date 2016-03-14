#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-10
#Authoruis:     kun/

import sys
import common

class Core(object):
	
	def confirmMoudle(self, path, moudle):
		list = path.split('/')
		last = list[len(list) - 1]
		for ls in list:
			if cmp(ls, common.getFrameworkName()) is 0:
				if cmp(moudle, last) is 0:
					return 1
		return 0

		
	def load(self, moudle):
		flag = None
		for i in range(1, len(sys.path)):
			if self.confirmMoudle(sys.path[i], moudle):
				obj =  __import__(moudle)
                		cls = getattr(obj, moudle)
                		cls.accpt(cls,moudle)
				flag = 1
				break;
				
		if flag is None:
			print "模块不存在！"


	def initParam(self,argv):
		print argv
		
