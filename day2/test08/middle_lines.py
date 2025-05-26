#!/usr/bin/env python3
import sys

file=sys.argv[1]
allLine=[]
with open(file,'r')as f:
    count=0
    for line in f:
        line=line.strip()
        allLine.append(line)
        count +=1
if count%2==0:
    mid1=count//2
    mid2=count//2 -1
    print(allLine[mid2])
    print(allLine[mid1])
else:
    mid1=count//2
    print(allLine[mid1])
# print(count)