#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-09
#Authoruis:     kun/

import sys
import getopt
import output
from core import Core

class Controller(object):

	def Usage():
		print 'TODO: help .',sys.path[0]
	#核心命令
	param = ['load', 'info', 'show', '-h', 'help', '--help']	
	help = ['-h', 'help', '--help']
	core = Core()

	#根据参数分配到指定处理方法
	def control(self, argv):
		argv = argv.split()
		if argv[0] in self.param:
			if argv[0] in self.help:
				Usage()
			elif len(argv) >= 2:
				if cmp(argv[0], 'load') is 0:
					self.core.load(argv[1])
				elif cmp(argv[0], 'info') is 0:
					print 'info .'
			else:
					print 'TODO:帮助信息', sys.path[0]
	

	def accept(self):
	        cmd = None
       		while(True):
                	if cmd is None:
                        	cmd = raw_input("\033[1;31;40mnearsec\033[0m:" + "\033[1;34;40m" + sys.path[0] + "\033[0m# ")
                	else:
                                self.control(cmd)
                        	cmd = None
			
