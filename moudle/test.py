#!/usr/bin/python  

import sys,os,re,unittest
  
def main():
	path = sys.path[0]
	sys.path.append("/usr/develop/git/nearsec/moudle")
	check =  __import__('check')
	print check
	clas = getattr(check, "Check")
	clas.command()
	#print sys.modules()['check']
	#print globals()
"""	obj = Print()  
  
	func_name = "do_foo"  
	static_name = "static_foo"  
	eval(func_name)()  
	getattr(obj, func_name)()  
	getattr(Print, static_name)()  
  
	func_name = "do_bar"  
	static_name = "static_bar"  
	eval(func_name)()  
	getattr(obj, func_name)()  
	getattr(Print, static_name)()  
  """
if __name__ == '__main__':  
	main()  
