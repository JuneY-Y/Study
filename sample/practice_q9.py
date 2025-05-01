#!/usr/bin/env python3
'''
字符数就是一行中所有字符的总数量，
包括字母、空格、标点符号等，但不包括行末的换行符 \n
'''
import sys


n=int(sys.argv[1])
filename=sys.argv[2]

with open(filename, 'r') as f:
    lines=f.readlines() ##read every line

new_lines=[]

for line in lines:
    line = line.rstrip('\n')

    while True:
        if len(line) <= n:
            new_lines.append(line)
            break
        
        if ' ' not in line:
            new_lines.append(line)
            break
        
        front=line[:n]
        ##🌟
        if ' ' in front:
            split_index=front.rfind(' ')
            new_lines.append(line[:split_index])
            line=line[split_index+1:]
            continue
        ##🌟
        split_index=line.find(' ')
        new_lines.append(line[:split_index])
        line=line[split_index+1:]
        continue

with open(filename, 'w') as f:
    for l in new_lines:
        f.write(l + '\n')