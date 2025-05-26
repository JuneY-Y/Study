#!/usr/bin/env python3

import sys
import re

# 读入输入行
lines = sys.stdin.readlines()

# 提取数字
numbers = []
for line in lines:
    num = re.findall(r'[+-]?(?:[0-9]+\.?[0-9]*|\.[0-9]+)', line)
    float_num = list(map(float, num))
    numbers.append(float_num)

# 每行最大值
Max = []
for num_list in numbers:
    try:
        line_max = max(num_list)
        Max.append(line_max)
    except ValueError:
        pass  # 这一行没有数字，跳过

# 所有行中最大值
try:
    all_max = max(Max) #不要起冲突的变量名
    # 打印包含最大值的行
    for idx, num_list in enumerate(numbers):
        if all_max in num_list:
            print(lines[idx], end='')
except ValueError:
    pass