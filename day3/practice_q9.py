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
    while len(line)>n: #用while循环进行分块
        if ' ' not in line:
            newline.append(line)
            break
        front=line[:n] #这个切片不理解
        if ' ' in front:
            index=front.rfind(' ')
            # left=line[:index]
            # right=line[index+1:]
            newline.append(line[:index])
            line=line[index+1:]
        else:
            index=line.find(' ')
            newline.append(line[:index])
            line=line[index+1:]
        if len(line)<=n:
            newline.append(line)

with open(file, 'w') as f:
    for l in newline:
        f.write(l+'\n')

