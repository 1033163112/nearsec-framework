#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-12
#Authoruis:     kun/

import sys

def exitCtrlC():
	status = raw_input('\n是否退出(Y/N):')
        if cmp(status.lower(),'y') is 0:
                sys.exit(1)


if __name__ == '__main__':
        getProjectName()
 

