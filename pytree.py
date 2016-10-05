#!/usr/bin/env python3
import subprocess
import sys
import os
import string
import re


def printName(indent, i, lastElement):
    if i == lastElement:
        print(indent + '└── ' + str(i))
        indent1 = indent + '    '
    else:
        print(indent + '├── ' + str(i))
        indent1 = indent + '│   '
    return indent1


def sort_key(s):
    return re.sub('[^A-Za-z]+', '', s).lower()


def sortList(curList):
    curList = [item for item in curList if item[0] != ('.')]
    curList = sorted(curList, key=sort_key)
    return curList



def printDir(path, file_cnt, dir_cnt, indent=''):
    if (path[-1] != '/'):
        path = path + '/'
    curList = os.listdir(path)
    curList = sortList(curList)
    cnt = []
    for i in curList:
        curPath = path + i
        if (os.path.isdir(curPath)):
            curPath = curPath + '/'
            dir_cnt = dir_cnt + 1
            indent1 = printName(indent, i, curList[-1])
            cnt1 = printDir(curPath, file_cnt, dir_cnt, indent1)
            file_cnt = cnt1[1]
            dir_cnt = cnt1[0]
        elif(os.path.isfile(curPath)):
            printName(indent, i, curList[-1])
            file_cnt = file_cnt + 1
    cnt.append(dir_cnt)
    cnt.append(file_cnt)
    return cnt


if __name__ == '__main__':

    subprocess.run(['tree'] + sys.argv[1:])
    if (len(sys.argv) == 1):
        path = '.'
    else:
        path = sys.argv[1]
    print(path)
    cnt = printDir(path, 0, 0, '')
    print()
    print('%d directories, %d files' % (cnt[0], cnt[1]))
