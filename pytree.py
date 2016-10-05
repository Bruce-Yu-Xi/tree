#!/usr/bin/env python3
import subprocess
import sys
import os

indent = '│   '
indent_done = '    '
child_branch = '├── '
child_branch_done = '└── '
fcount = 0
pathcount = 0


def tree_generate(path, symbol):
    global dircount
    global filecount
    alld = []
    for i in os.listdir(path):
        if not i.startswith('.'):
            alld += [i]
    alld.sort(key=lambda s: s.strip('_').lower())
    end = False
    num = 0
    for children in alld:
        if(num < (len(alld) - 1)):
            print(symbol + child_branch + str(children))
        else:
            end = True
            print(symbol + child_branch_done + str(children))
        if (os.path.isdir(os.path.join(path, children))):
            pathcount += 1
            if end:
                tree_generate(os.path.join(path, children), symbol + indent_done)
            else:
                tree_generate(os.path.join(path, children), symbol + indent)
        elif(os.path.isfile(os.path.join(path, children))):
            fcount += 1
        num += 1

if __name__ == '__main__':
    dir_path = "."
    if(len(sys.argv) == 2):
        dir_path = sys.argv[1]
    print(dir_path)
    tree_generate(dir_path, "")
    print()
    print(str(pathcount) + " directories, " + str(fcount) + " files")
