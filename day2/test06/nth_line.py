#!/usr/bin/env python3
'''
🌟重点
需要进一步理解 for i in range(n)
这里非常值得练习,因为很基础但是能领悟很多的,我有点儿模糊的知识点
'''
import sys
n=int(sys.argv[1])
file=sys.argv[2]

#-----readline+
	# •	f.readline() → 每次只读一行
	# •	如果提前遇到 EOF（文件行数不足 n），line 会变成 ''，我们用 if not line 捕获
	# •	最后只在 line 有内容时才 print
with open (file, 'r') as f:
    line=None
    for i in range(n):
        line=f.readline()
        if not line:
            line=None
            break
if line:
    print(line, end='')

#这里最值得一提的是：
# with open(file, 'r')as f:
#     lines=f.readlines()
# if n<=len(lines):
#     print(lines[n-1], end='')

# with open(file, 'r') as f:
#     for idx, line in enumerate(f, start=1):
#         if idx==n:
#             print(line, end='') ## line 会自带\n
#             break