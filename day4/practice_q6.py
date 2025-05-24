#!/usr/bin/env python3
#这道题是有坑的，对于具体到哪一行不对应，和条件判断的时候需要输入进list里
#为什么要list？

import sys
flag=0
with open(sys.argv[1],'r') as f1:
    line1=f1.readlines()
    len1=len(line1)

# print(len1)
with open(sys.argv[2],'r') as f2:
    line2=f2.readlines()
    len2=len(line2)
line22=list(reversed(line2)) # e.g. the lines can be read into a list.
if (len1!=len2):
    print(f"Not mirrored: different number of lines: {len1} versus {len2}")
    flag=1
elif line1==line22:
    print("Mirrored")
else:
    for i in range(len1):# 这里bug了下
       if line1[i] != line2[-1-i]:#这里卡住了
            print(f"Not mirrored: line {i+1} different")
            sys.exit(0)

# line22=list(reversed(line2)) # e.g. the lines can be read into a list.
# if (flag==1):
#     for i in range(len1):
#        if line1[i] != line2[-1-i]:
#             print(f"Not mirrored: line {i+1} different")
#             sys.exit(0)

# if len(lines1)!=len(lines2):
#     print(f"Not mirrored: different number of lines: {len(lines1)} versus {len(lines2)}")
# elif lines1 == list(reversed(lines2)): # ✔️ 先把 iterator 转换成 list
#     print("Mirrored")
# else:
#     for i in range(len(lines1)):#❌没想道
#         if lines1[i] != lines2[-1-i]:
#             print(f"Not mirrored: line {i+1} different")
#             sys.exit(0)
            

# print(len2)
# print(len1,len2)