#!/usr/bin/env python3

import sys
n=int(sys.argv[1])
file=sys.argv[2]

with open(file, 'r')as f:
    lines=f.readlines()

newline=[]
for line in lines:
    line=line.rstrip()
    # newline=[]
    if len(line)>n:
        if " " not in line:
            newline.append(line)
            continue
        else:
            index=line.rfind(' ')
            left=line[:index]
            right=line[index+1:]
            newline=newline.append(left)
    else:

