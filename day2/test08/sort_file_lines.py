#!/usr/bin/env python3
import sys
file=sys.argv[1]
## 不能单独收集
# compare=[]
# l=[]
with open (file, 'r') as f:
    line=f.readlines() #readlines() 会自动把每一行，包括结尾 \n，作为独立字符串读进列表
    # for lines in line:
    #     compare.append(len(lines))
    #     l.append(lines)
#sorted排序
sorted_lines=sorted(line,key=lambda x: (len(x),x))
        
for l in sorted_lines:  #排序后的结果直接循环
    print(l, end='') #保留原始换行符🌟