#!/usr/bin/env python3

    # •	查找每一行中出现的数字（包括 负数、小数、整数）
	# •	找出包含 最大数字 的所有行（可能会有多行）
	# •	最后把这些行 按出现顺序 输出
	# •	如果所有行都没有数字，则输出为空

# 解决办法
# 	•	使用 defaultdict 实现按数字归类
# 	•	正则表达式高效匹配
# 	•	最后 max() 提取最大值并输出对应行
import sys
import re
from collections import defaultdict
# Dictionary: number -> list of lines that contain it
counter = defaultdict(list)
for line in sys.stdin:
    for num in re.findall(r'[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)', line):
         # Convert matched number to float and record the line
        counter[float(num)].append(line)

# Print all lines that contain the max number (in order)
if counter:
    max_num = max(counter)
    for line in counter[max_num]:
        print(line, end='')