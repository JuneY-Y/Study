#!/usr/bin/env python3

import sys
n=int(sys.argv[1])
file=sys.argv[2]

with open(file, 'r')as f:
    lines=f.readlines()

for line in lines:
    line=line.rstrip()
    if len(line)>n:

    else: