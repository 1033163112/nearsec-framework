#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:	0.01
#Create:	2016-01-07
#Authoruis:	kun/

import readline
import sys
import getopt
import sys
import os
import core
import exception
import common
import log

class Moudle(object):
	runInfo = {
	 	'longOpts':['help'],
        	'shortOpts':'hv',
        	'help':'help',
        	'version':'version 1.0'
	}
	
	@staticmethod	
	def usage(self):
		print self.runInfo['help']

	@staticmethod
	def version(self):
		print self.runInfo['version']
 
	def __init__(self):
		log.todo('init moudle ' + os.path.abspath(sys.argv[0]))
	
	@staticmethod
        def accpt(self, moudle):
                cmd = None
                while(True):
                        if cmd is None:
				try:
                                	cmd = raw_input("\033[1;31;40mnearsec@" + moudle + "\033[0m" + ":" + "\033[1;34;40m" + sys.path[0] + "\033[0m# ")
                        	except KeyboardInterrupt:
					common.exitCtrlC()
			else:
				if self.start(self, cmd):
					break
                                cmd = None

	@staticmethod
	def start(self, argv):
		try:
			options,args = getopt.getopt(argv.split(' '), self.runInfo['shortOpts'], self.runInfo['longOpts'])
		except getopt.GetoptError, e:
			self.start('-h')
		for n,v in options:
			log.debug(n,v)
			if n in ('-h', '--help'):
				self.usage(self)
			elif n in ('-v', '--version'):
				self.version(self)
			elif n in ('back',''):
				return 1
			else:
				self.moudleConsole(self, args)
		

	@staticmethod
	def moudleConsole(self, argv):
		log.todo('自定义参数控制执行流程 ' + os.path.abspath(sys.argv[0]))
