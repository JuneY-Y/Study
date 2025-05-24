#!/usr/bin/env python3
## takes two command line argument, a positive integer n and the name of a file.

import sys
n=sys.argv[1]
file=sys.argv[2]

with open (file,'r') as f:
    # lines=[line for line in f]
    for line in f:
        line=line.strip()
new_lines=[]

while len(line)>n:
    if ' ' not in line: #这里用了not in 来进行判断
        new_lines.append(line)
        break
    front=line[:n] #n之前的
    if ' ' in front:
        split_index=front.rfind(' ')
        new_lines.append(line[:split_index])
        line=line[split_index+1:]

