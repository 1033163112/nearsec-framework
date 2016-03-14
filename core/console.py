#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-07
#Authoruis:     kun/

import sys
import getopt
import output 
from controller import Controller


def console(argv):
	control = Controller()
	control.accept()
	sys.exit(1)

if __name__ == '__main__':
	main(sys.argv)


