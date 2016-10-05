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


def printDir(dir, file_cmd, dir_cmd, indent=''):
    if (dir[-1] != '/'):
        dir += '/'
    curList = os.listdir(dir)
    curList = sortList(curList)
    cmd = []
    for i in curList:
        curDir = dir + i
        if (os.path.isdir(curDir)):
            curDir += '/'
            dir_cmd += 1
            indent1 = printName(indent, i, curList[-1])
            cmd1 = printDir(curDir, file_cmd, dir_cmd, indent1)
            file_cmd = cmd1[1]
            dir_cmd = cmd1[0]
        elif(os.path.isfile(curDir)):
            printName(indent, i, curList[-1])
            file_cmd += 1
    cmd.append(dir_cmd)
    cmd.append(file_cmd)
    return cmd


if __name__ == '__main__':
    size = len(sys.argv)
    if  size == 1:
        dir = '.'
    else:
        if size == 2:
            dir = sys.argv[1]
        else:
            print('ERROR')
    print(dir)
    cmd = printDir(dir, 0, 0, '')
    print('%d directories, %d files' % (cmd[0], cmd[1]))
