#!/usr/bin/env python3
import sys

file=sys.argv[1]

with open(file,'r')as f:
    for line in f:
        line=line.strip()
        print(line)
        length=len(line)

print(length)