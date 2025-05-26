#!/usr/bin/env python3
'''
✅ 按行读入输入
✅ 每行提取或处理部分内容
✅ 逐步比较、更新一个“全局最优值”
✅ 最终输出与全局最优值相关的行/结果
'''
import re
import sys

max_value = None
lines_with_max = []

for line in sys.stdin:
    line = line.rstrip('\n')
    numbers = re.findall(r'-?\d+(?:\.\d+)?', line)  # 改进正则：支持负数和小数
    numbers = [float(num) for num in numbers]

    if numbers:
        line_max = max(numbers)
        if (max_value is None) or (line_max > max_value):
            max_value = line_max
            lines_with_max = [line]  # 新最大，重置列表
        elif line_max == max_value:
            lines_with_max.append(line)  # 相同最大，加入列表

if max_value is not None:
    for l in lines_with_max:
        print(l)
