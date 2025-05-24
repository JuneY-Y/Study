#!/usr/bin/env python3
import sys

file1=sys.argv[1]
file2=sys.argv[2]

print(file1)
lens1=file1.readline()
print(lens1)

for line in file2:
    lens2=line.readline()
print(lens2)
