#!/usr/bin/env python3
# ==============================================================================
# name: final_q5.py
# aim: Read from stdin, swap first and last integer in a line (if >=2 integers)
#
# Written by: JiamingYang z5452842
# Date: 2025-04-07
# For COMP2041/9044

# 考点: 必须记住的: 找到整数 re.finditer(r'-?\d+', line)
#\d为 [0-9] 任意一个digit
# + 是正则的重复符号，意思是：前面的东西重复 1 次或多次
# ==============================================================================

import sys
import re

for line in sys.stdin: # ✅
    line = line.rstrip('\n')  # 去掉换行符

    # 使用正则找到所有整数 正确想法： 🌟正则以后切片连接
    matches = list(re.finditer(r'-?\d+', line))  #re.finditer ?? finditer是什么

    if len(matches) < 2:
        # 少于两个整数 → 原样输出
        print(line)
    else:
        # 交换第一个和最后一个整数
        first = matches[0]
        last = matches[-1]

        # 提取整数字符串
        first_num = first.group()
        last_num = last.group()

        # 替换它们的位置
        # 注意：要按位置替换，为了不影响索引顺序，从右往左替换
        new_line = (
            line[:last.start()] +
            first_num +
            line[last.end():]
        )
        new_line = (
            new_line[:first.start()] +
            last_num +
            new_line[first.end():]
        )

        print(new_line)

# with open (swap_numbers.txt, 'r') as f:
#     for line in sys.stdin:
#         for integer in line:
#             swap(line(0), line(n-1))
#             print()