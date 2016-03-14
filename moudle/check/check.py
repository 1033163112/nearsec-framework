#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-08
#Authoruis:     kun/

from core.moudle import Moudle
import sys

class check(Moudle):
	
	def __init__():
		print "check init ."
	
	@staticmethod
	def moudleConsole(self, argv):
		print 'diyConsole !',sys.path[0]
