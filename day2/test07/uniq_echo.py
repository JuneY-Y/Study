#!/usr/bin/env python3
'''
1️⃣ 把 set 变成 列表（因为 set 没顺序，最好用 list 保序）
2️⃣ 用 ' '.join() 拼接成字符串
改进:
	•	result.append(arg) → 把第一次出现的参数按顺序存起来
	•	' '.join(result) → 用空格拼接成一行字符串输出
	•	最后不用 end=''，因为整个 print 一次性输出好

'''
import sys
# from collections import Counter
seen=set()
result=[]
# for i, file in enumerate(sys.argv[+1:]):
#     print(f"{i} {file}")
for arg in sys.argv[+1:]:
    if arg not in seen:
        # print(arg, end='')  ##很多次都需要end='', 什么时候会用到
        seen.add(arg)
        result.append(arg)

print(' '.join(result))