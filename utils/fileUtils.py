#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:	0.01
#Create:	2016-03-12
#Authoruis:	kun/

import os


list = []
#遍历目录/子目录下所有文件
def traversal_dir(filepath, prin=False):
	#遍历filepath下所有文件，包括子目录
	files = []
	try:
		files = os.listdir(filepath)
	except OSError:
		pass
		print filepath,"\t The folder does not exist!"
	if len(files):
		for fi in files:
			fi_d = os.path.join(filepath,fi)            
			if os.path.isdir(fi_d):
				traversal_dir(fi_d, prin)        
			else:
				if prin :
					print os.path.join(filepath,fi_d)
				list.append(os.path.join(filepath,fi_d))#添加遍历到的文件
	return list

#遍历指定目录下所有文件夹
def iteratorDir(path):
	dirPathList = []
	try:
                fileList = os.listdir(path)
		path = '/usr/develop/git/nearsec/moudle/'
        	for file in fileList:
                	if os.path.isdir(path + file):
                        	dirPathList.append(path + file)
		return dirPathList

        except OSError:
                pass
                print filepath,"\t The folder does not exist!"




def test():
	#递归遍历所有文件
	print iteratorDir('/usr/develop/git/nearsec/')

if __name__ == '__main__':
	test()

