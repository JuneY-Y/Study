#!/usr/bin/env python3
#这道题需要重新琢磨一下，并且看看考点是什么
#test8 是个坑，题目中说只输出一行不对的，因此输出一行即可
#还是需要读题的
import sys

file1=sys.argv[1]
file2=sys.argv[2]

with open(file1) as f1, open(file2) as f2:
    lines1=[line.rstrip('\n') for line in f1] ##每个处理的都需要\n
    lines2=[line.rstrip('\n') for line in f2]

if len(lines1)!=len(lines2):
    print(f"Not mirrored: different number of lines: {len(lines1)} versus {len(lines2)}")
elif lines1 == list(reversed(lines2)): # ✔️ 先把 iterator 转换成 list
    print("Mirrored")
else:
    for i in range(len(lines1)):#❌没想道
        if lines1[i] != lines2[-1-i]:
            print(f"Not mirrored: line {i+1} different")
            sys.exit(0)
            