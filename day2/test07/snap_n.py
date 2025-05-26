#!/usr/bin/env python3
'''
考察sys.stdin
再写一遍
'''
import sys

n = int(sys.argv[1])
counts = {}

for line in sys.stdin:
    line = line.rstrip('\n')
    counts[line] = counts.get(line, 0) + 1  #	counts.get(line, 0) + 1 → 如果没见过，就是 1；见过就 +1
    if counts[line] == n:
        print(f"Snap: {line}")
        break
# result=[]
# n=sys.argv[1]
# for line in sys.stdin:
#     line=line.rstrip('\n')
#     result.append(line)
#     if line in result:
#         for i in range(n):
            
#     else
#         continue