#!/usr/bin/env python3
import sys

with open(sys.argv[1],'r') as f1:
    line1=f1.readlines()
    len1=len(line1)

print(len1)
with open(sys.argv[2],'r') as f2:
    line2=f2.readlines()
    len2=len(line2)

if (len1!=len2):
    print(f"Not mirrored: different number of lines: {len1} versus {len2}")
else:
    print("Mirrored")

print(len2)
# print(len1,len2)