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
        	for file in fileList:
                	if os.path.isdir(path + file):
                        	dirPathList.append(path + file)
		return dirPathList

        except OSError:
                pass
                print filepath,"\t The folder does not exist!"


#读取文件 返回值:整个文件内容 
def read(filepath):
	text = ''
	try:
		file_object = open(filepath)
		text = file_object.read()
		file_object.close()
	except IOError:
		pass
		print filepath, "\topen fail !"
		text = -1
	return text

#读取文件 返回值:list
def readRetList(filepath):
	ls = []
	try:
		file_object = open(filepath)
	except IOError:
		pass
	while 1:
		line = file_object.readline()
		if not len(line):
			break
		ls.append(line.strip("\n"))
	file_object.close()
	return ls
	

#将text写入文件
def write(filepath, text, type):
	file_object = open(filepath, type)
        try:
                file_object.write(text)
        finally:
                file_object.close()

#将一个list写入文件，无换行
def writeList(filepath, list, type):
	file_object = open(filepath, type)
        try:
                file_object.writelines(list)
        finally:
                file_object.close()



#查找filepath文件内容是否包含str字符串 
#不包含返回	-1
def find(filepath, str):
	file_text = read(filepath)
	return file_text.lower().find(str.lower())

#文件中查找集合中的字符串，返回值：strList中字符串在文件中存在的数量
def findListStr(filepath, strList):
	flag = 0
	file_text = read(filepath)
	if file_text != -1:
		for str in strList:
			if file_text.lower().find(str.lower()) != -1:
				print str , "\t\t==>",filepath
				if flag:
					flag += flag
				else:
					flag = 1
			file_text.lower().find(str.lower())
	return flag

def test():	
	print read("../dictionaries/rule.txt")


if __name__ == '__main__':
	test();

