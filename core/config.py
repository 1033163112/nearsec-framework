#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-10
#Authoruis:     kun/

import sys

import test
import common
from utils import fileUtils

class Config(object):
	
	def getProjectPath():
		ls = fileUtils.readRetList('../data/conf/nearsec.conf')
