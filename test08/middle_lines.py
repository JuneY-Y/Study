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
if count==0: ### 如果什么都没有输入。那么直接exit(0)
    exit(0)
else:
    if count%2==0:
        mid1=count//2
        mid2=count//2 -1
        print(allLine[mid2])
        print(allLine[mid1])
    else:
        mid1=count//2
        print(allLine[mid1])  #allLine[1] 就是文件的第 2 行（因为从索引 0 开始）
# print(count)
# #!/usr/bin/env python3

# from sys import argv

# # ifodd
# # ifeven
# with open(argv[1], "r") as f:
#     lines=f.readlines()

#     if lines:
#         length=len(lines)
#         if length%2==1:
#             print(lines[length//2], end="")
#         else:
#             print(lines[(length//2)-1], end="")
#             print(lines[length//2], end="")


