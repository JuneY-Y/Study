#!/usr/bin/env python3
import sys

file1=sys.argv[1]
file2=sys.argv[2]

with open(file1) as f1, open(file2) as f2:
    lines1=[line.rstrip('\n') for line in f1]
    lines2=[line.rstrip('\n') for line in f2]

if len(lines1)!=len(lines2):
    print(f"Not mirrored: different number of lines: {len(lines1)} versus {len(lines2)}")