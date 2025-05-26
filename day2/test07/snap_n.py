#!/usr/bin/env python3
'''
考察sys.stdin
'''
import sys
result=[]
n=sys.argv[1]
for line in sys.stdin:
    line=line.rstrip('\n')
    result.append(line)
    if line in result:
        print()