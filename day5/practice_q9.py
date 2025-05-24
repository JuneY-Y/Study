#!/usr/bin/env python3
'''
	•	特殊条件：比如“不超过 n 不用改”“无空格不改”
	•	优先级：比如先按前 n 个找空格，找不到再全行找

'''
import sys
#which takes two command line argument, n and name of a file
n=int(sys.argv[1])
filename=sys.argv[2]

with open(filename, 'r') as f:
    lines=f.readlines()

new_lines=[]
for line in lines:
    line=line.rstrip('\n')

    while len(line)>n:
        if ' ' not in line:
            new_lines.append(line)
            break
        front=line[:n]
        if ' ' in front:
            split_index=front.rfind(' ') #rfind不熟悉
            new_lines.append(line[:split_index])
            line=line[split_index+1:]
        else:
            split_index=line.find(' ')
            new_lines.append(line[:split_index])
            line=line[split_index+1:]
    if len(line)<=n:
        new_lines.append(line)
with open(filename, 'w') as f:
    for l in new_lines:
        f.write(l + '\n')