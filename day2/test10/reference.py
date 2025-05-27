#!/usr/bin/env python3
'''
总结：	
    •	stdin 按行读入
	•	按列分割处理
	•	按条件过滤行
	•	按内容排序输出
    具体：
	•	for line in sys.stdin: → 直接按行读入。
	•	rstrip('\n') → 只去掉换行，不误删行内空格。
	•	print(line) → 默认会自动换行，所以不需要 end=''。
	•	re.search(r'#\d+', line) → 检查是否包含 # 后跟数字（如 #7）。
'''
import sys
import re

for line in sys.stdin: #output: line A\n
    line = line.rstrip('\n')  # output :line A 只去掉换行，不去掉前后空格
    if not re.search(r'#\d+', line):
        print(line)
# for file in sys.stdin:
#     lines=file.strip('\n') ## 只去换行
#     for line in lines: ## 🌟按字符便利
#         if not re.search(r'#\d+',line):
#             print(line,end='')
    # print('\n')
    # print(lines)
    

    