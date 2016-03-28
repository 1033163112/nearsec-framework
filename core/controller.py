#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-09
#Authoruis:     kun/

import sys
import os
import getopt
import output
from core import Core
from core import common
import log

class Controller(object):

	core = Core()#获取核心对象
	
	#帮助信息
	def Usage(self):
		log.todo('help ' + os.path.abspath(sys.argv[0]))

	#框架控制台基础命令
	param = ['load', 'info', 'show', '-h', 'help', '--help', 'exit', 'quit']	
	help = ['-h', 'help', '--help']

	#根据参数分配到指定处理方法
	def control(self, argvs):
		argv = argvs.split()
		if len(argv) is 0:
			return 
		if argv[0] in self.param:
                        if argv[0] in ('exit', 'quit'):
				sys.exit(1)
			elif argv[0] in self.help:
				self.Usage()
			elif len(argv) >= 2:
				if cmp(argv[0], 'load') is 0:
					self.core.load(argv[1])
				elif cmp(argv[0], 'info') is 0:
					print 'info .'
		else:
                        log.todo('提示信息 1' + os.path.abspath(sys.argv[0]))

	
	#接收参数
	def accept(self):
	        cmd = None
       		while(True):
                	if cmd is None:
				try:
                        		cmd = raw_input("\033[1;31;40mnearsec\033[0m:" + "\033[1;34;40m" + sys.path[0] + "\033[0m# ")
	                	except KeyboardInterrupt,e:
                                        common.exitCtrlC()

			else:
                                self.control(cmd)
                        	cmd = None
			
