#!/usr/bin/env python3
import subprocess
import sys
import os

indent = '│   '
indent_done = '    '
child_branch = '├── '
child_branch_done = '└── '
file_count = 0
dir_count = 0


def tree_generate(path, symbol):
    global dir_count
    global file_count
    all_children = sorted([c for c in os.listdir(path) if not c.startswith('.')], key=lambda s: s.strip('_').lower())
    end_file = 0
    num_children = 0
    for children in all_children:
        if(num_children < (len(all_children) - 1)):
            print(symbol + child_branch + str(children))
        else:
            end_file = 1
            print(symbol + child_branch_done + str(children))
        if (os.path.isdir(os.path.join(path, children))):
            dir_count = dir_count + 1
            if(end_file == 1):
                tree_generate(os.path.join(path, children), symbol + indent_done)
            else:
                tree_generate(os.path.join(path, children), symbol + indent)
        elif(os.path.isfile(os.path.join(path, children))):
            file_count = file_count + 1
        num_children = num_children + 1

if __name__ == '__main__':

    subprocess.run(['tree'] + sys.argv[1:])
    dir_path = "."
    if(len(sys.argv) == 2):
        dir_path = sys.argv[1]
    print(dir_path)
    tree_generate(dir_path, "")
    print()
    print(str(dir_count) + " directories, " + str(file_count) + " files")
