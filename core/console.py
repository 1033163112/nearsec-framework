#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-07
#Authoruis:     kun/

import test
import sys
import getopt
import output 
import common
from controller import Controller

class Console(object):

	#框架基础命令
	basic = {
		'longOpts':['help'],
                'shortOpts':'hv',
		'extend' :['load', 'back', 'exit']
	}

	custom  = {
		'longOpts':[''],
                'shortOpts':''	
	}

	#框架提示信息
	info = {
                'help':'help',
                'version':'version 1.0'
        }
	
	def usage(self):
                print self.info['help']

        def version(self):
                print self.info['version']


	def accpt(self, cmdLine):
                cmd = None
                while(True):
                        if cmd is None:
                                try:
                                        cmd = raw_input(cmdLine)
                                except KeyboardInterrupt:
                                        common.exitCtrlC()
                        else:
				if cmd.strip() is 'back':
					break
				if self.basicConsole(cmd) is 1:
                                	self.console(cmd)
                        cmd = None
	
	#检测框架命令行状态（主控制台、模块控制台）
	def checkShell():
		print '检测当前shell的状态，是在什么权限下'

	#执行自定义命令
	def customConsole(self, cmd):
		try:
                        options,args = getopt.getopt(cmd.split(' '), self.basic['shortOpts'], self.basic['longOpts'])
                except getopt.GetoptError, e:
                	customConsole('-h')
		basicConsole('-h')

	#执行框架核心命令,命令不存在返回0
	def basicConsole(self, cmd):
		extend = self.basic['extend']
		cmd = cmd.strip()
		if cmp(cmd, extend[0]) is 0:
			print 'load'
		elif cmp(cmd, extend[2]) is 0:
			sys.exit(0)
                elif cmd in ('-h', '--help'):
			self.usage()
		elif cmd in ('-v', '--version'):
			self.version()
		else:
			self.moudleConsole(self, args)
		return 0		


if __name__ == '__main__':
	cons = Console()
	cons.accpt('test #')


