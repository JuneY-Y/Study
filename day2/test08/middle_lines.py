#!/usr/bin/env python3
import sys

file=sys.argv[1]

with open(file,'r')as f:
    count=0
    for line in f:
        line=line.strip()
        count +=1
        if count%2==0:
            print("Even")
        else:
            print("Odd")

print(count)