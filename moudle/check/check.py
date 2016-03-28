#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-08
#Authoruis:     kun/

import os
import sys
from core.moudle import Moudle
from core import log

class check(Moudle):
	
	def __init__():
		print "check init ."
	
	runInfo = {
                'longOpts':['help','test'],
                'shortOpts':'hvt',
                'help':'help',
                'version':'check 0.1'
        }

	"""
	自定义控制台
	"""
	@staticmethod
	def moudleConsole(self, argv):
		print argv
		log.todo('moudleConsole ')
