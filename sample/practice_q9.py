#!/usr/bin/env python3
'''
1. 每行都判断长度是否 > n：
   - 如果不是，直接保留
   - 如果超过 n 个字符：
     → 尝试从前 n 个字符中找最后一个空格（优先按单词换行）
     → 找不到就强制以第一个空格截断（长单词情况）
2. 将新行写回文件，换行符加回去
笔记📒
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