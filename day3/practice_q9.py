#!/usr/bin/env python3
'''
.append() 会直接修改原列表并返回 None!
append 不返回新列表，而是就地修改
'''
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
    if len(line)<=n: # 循环结束以后，继续把<n也就是符合切片要求的代码写入newline里面
        newline.append(line)

with open(file, 'w') as f:
    for l in newline:
        f.write(l+'\n')

