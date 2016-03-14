#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.01
#Create:        2016-03-07
#Authoruis:     kun/

USAGE_TEXT = """\033[1;35;40m
nearsec - 服务器安全工具集\033[0m

Usage:
	 nearsec -h

Options:
	-h or --help
	     显示帮助信息 
	-s <文件路径> or --path=<文件路径>
	     扫描指定路径
	-t <线程数> or --thread=<线程数>
             指定运行线程数
	-v or --version
	     获取nearsec当期VERSION 
"""
VERSION = """
nearsec - 服务器安全工具集
\033[1;34;40m
版本: debug 0.1
\033[0m
作者: kun
"""
EMPTY_MSG = """
请输入参数
"""
#打印并返回字符串（红色）
def print_red(str):
	print red(str)
	return red(str)

#将传入字符串染色（红色）
def red(str):
	return "\033[1;31;40m" + str + "\033[0m"

#打印并返回字符串（绿色）
def print_green(str):
	print green(str)
	return green(str)

#将传入字符串染色（绿色）
def green(str):
        return "\033[1;32;40m" + str + "\033[0m"

