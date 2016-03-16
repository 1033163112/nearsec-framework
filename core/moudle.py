#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:	0.01
#Create:	2016-01-07
#Authoruis:	kun/

import readline
import sys
import getopt

import core
import exception
import common

class Moudle(object):
	runInfo = {
	 	'longOpts':'test=',
        	'shortOpts':'hv',
        	'help':'help',
        	'version':'check 0.1'
	}
	
	@staticmethod	
	def usage(self):
		print self.runInfo['help']

	@staticmethod
	def version(self):
		print self.runInfo['version']
 
	def __init__(self):
		print "init Controller ."
	
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
		args = argv.split()
		if len(args) is 1:
			if args[0] in ('-h', '--help'):
				self.usage(self)
			elif args[0] in ('-v', '--version'):
				self.version(self)
			elif args[0] in ('back',''):
				return 1
			else:
				self.usage(self)
		else:
			self.diyConsole(self, args)
	@staticmethod
	def moudleConsole(self, argv):
		print 'diy .', agrv
