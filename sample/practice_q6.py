#!/usr/bin/env python3

import sys
'''
用途：验证两个文本文件是否为镜像关系。
技巧：倒序索引、字符串剥离、逐行比较。
输入：两个文件名参数。
输出：若不一致，指出哪一行不同；若一致，输出 "Mirrored"。
'''

file1=sys.argv[1]
file2=sys.argv[2]

with open (file1, 'r')  as f1:
    line1=[line.strip('\n') for line in f1]

with open (file2, 'r')  as f1:
    line2=[line.strip('\n') for line in f2]

#进行长度的匹配
if len(lines1) != len(lines2):
    print(f"Not mirrored: different number of lines: {len(lines1)} versus {len(lines2)}")
