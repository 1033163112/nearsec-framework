#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-23
#Authoruis:     kun/

import output
from utils import fileUtils

#输出debug信息
def debug(*messages):
	for msg in messages:
		output.print_red('[Debug] ' + msg)
		save('[Debug] ' + msg + '\n')

def error(*messages):
	for msg in messages:
		save('[Error] ' + msg + '\n')

def todo(*messages):
	for msg in messages:
                output.print_green('[TODO] ' + msg)


#记录日志
def save(msg):
	fileUtils.write('/usr/develop/git/nearsec-framework-master/data/log/debug.log', msg, 'a+')

if __name__ == '__main__':
	error('error')
