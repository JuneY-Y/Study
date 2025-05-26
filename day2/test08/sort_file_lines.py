#!/usr/bin/env python3
#需要再写一遍
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
# ✅ 排序 key 用 (len(x), x)，确保：
# 	•	先按长度
# 	•	如果长度一样，再按字母序
sorted_lines=sorted(line,key=lambda x: (len(x),x))
        
for l in sorted_lines:  #排序后的结果直接循环
    print(l, end='') #保留原始行内换行符🌟