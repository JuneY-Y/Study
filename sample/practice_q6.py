#!/usr/bin/env python3

import sys

# 抓取standin输入的内容为 $1 $2
file1 = sys.argv[1]
file2 = sys.argv[2]


#打开文件
with open (file1, 'r') as f1:
    lines1 = [line.rstrip('\n') for line in f1]

with open (file2, 'r') as f2:
    lines2 = [line.rstrip('\n') for line in f2]

if len(lines1) != len(lines2):
    print(f"Not mirrored: different number of lines: {len(lines1)} versus {len(lines2)}")
    sys.exit(0)

#reversed_lines1=list(reversed(lines1))

for i in range(len(lines1)):
    if lines1[i] != lines2[-(i+1)] : # file2逆序比较的方法
        print(f"Not mirrored: line {i+1} different")
        sys.exit(0)

print("Mirrored")
