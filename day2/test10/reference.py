#!/usr/bin/env python3
'''
总结：	这个代码非常值得学习，因为涉及到了很多的点:
    •	stdin 按行读入
	•	按列分割处理
	•	按条件过滤行
	•	按内容排序输出
    具体：
	•	for line in sys.stdin: → 直接按行读入。
	•	rstrip('\n') → 只去掉换行，不误删行内空格。
	•	print(line) → 默认会自动换行，所以不需要 end=''。
	•	re.search(r'#\d+', line) → 检查是否包含 # 后跟数字（如 #7)。
'''
#Lines of the form #n (where n is an integer value), should be replaced by the n’th line of input.
# 理解不了就直接带n进行赋值，即可
import sys
import re

lines=sys.stdin.readlines()

#保留行内空格，只去掉换行
for line in lines: 
    if line[-1] == '\n':
        line=line[:-1]
    #用正则匹
    m=re.fullmatch(r'#(\d+)', line)
    if m:
        # print(f"this is what I want to see{m.group(1)}")
        n=int(m.group(1))
        print(lines[n-1],end='') #自带换行符，所以要去掉
    else:
        print(line)
         # output :line A 只去掉换行，不去掉前后空格
    # if not re.fullmatch(r'#[0-9]\n', line):
    #     print(line)

    

    