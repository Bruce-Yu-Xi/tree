#!/usr/bin/python  
import os
import sys
import string  
class XXTree:
	def __init__(self):
		pass
	def getTree(self, dir):
		list = self.getList(dir, 0)  
		treelist = []  
		for i in range(0, len(list)):
			fullpath = list[i]  
			parpath = os.path.dirname(list[i])  
			filename = os.path.basename(list[i])  
			if(fullpath == dir):   
				treelist.append(fullpath)  
				continue  
                  	path = fullpath.replace(dir, "")  
			names = path.split("/")  
			name = "|--->" + names[len(names) - 1]  
			for j in range(1, len(names) - 1):  
				name = "    " + name  
			treelist.append(name)  
			pos = name.index("|")  
			j = i - 1  
			while j > 0:  
				name = treelist[j]  
				if(name[pos] == '|' or name[pos] == ' '):  
					name = name[0: pos] + "|" + name[pos + 1: len(name)]  
					treelist[j] = name  
				else:  
					break  
				j = j - 1  
		for i in range(0, len(treelist)):  
			print (treelist[i])  
	def getList(self, dir, layer):  
		list = []  
		if layer == 0: list.append(dir)  
		files = os.listdir(dir)  
		for file in files:  
			file = os.path.join(dir, file)  
			if os.path.isdir(file):  
				list.append(file)  
				list += self.getList(file, layer + 1)  
			else:  
				list.append(file)  
		return list  
t = XXTree()
if len(sys.argv) < 2 :  
	dir = './'  
else:     
	dir = sys.argv[1]
t.getTree(dir)
