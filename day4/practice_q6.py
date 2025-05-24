#!/usr/bin/env python3
import sys
flag=0
with open(sys.argv[1],'r') as f1:
    line1=f1.readlines()
    len1=len(line1)

print(len1)
with open(sys.argv[2],'r') as f2:
    line2=f2.readlines()
    len2=len(line2)

if (len1!=len2):
    print(f"Not mirrored: different number of lines: {len1} versus {len2}")
    flag=1
else:
    print("Mirrored")

if (flag==1):
    for lines1 in f1:
        liness1=lines1.strip()
        for lines2 in f2:
            liness2=reversed(lines2.strip())
            if (liness1!=liness2)


            

print(len2)
# print(len1,len2)