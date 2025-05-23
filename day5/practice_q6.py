#!/usr/bin/env python3
import sys

file1=sys.argv[1]
file2=sys.argv[2]

with open(file1) as f1, open(file2) as f2:
    lines1=[line.rstrip('\n') for line in f1]
    lines2=[line.rstrip('\n') for line in f2]

if len(lines1)!=len(lines2):
    print(f"Not mirrored: different number of lines: {len(lines1)} versus {len(lines2)}")
elif lines1 == list(reversed(lines2)): # ✔️ 先把 iterator 转换成 list
    print("Mirrored")
else:
    for i in range(len(lines1)):
        if lines1[i] != lines2[-1-i]:
            print(f"Not mirrored: line {i+1} different")
            