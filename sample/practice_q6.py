#!/bin/env/python3

import sys

# 抓取standin输入的内容为 $1 $2
file1 = sys.argv[1]
file2 = sys.argv[2]


#打开文件
with open (filename, 'r') as f1:
    line1 = [line.rstrip('\n') for line in f1]

with open (filename, 'r') as f2:
    line2 = [line.rstrip('\n') for line in f2]