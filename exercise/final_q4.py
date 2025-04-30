#!/usr/bin/env python3
# ==============================================================================
# name: find_two_enrolled.py 🌟 需要自己写
# aim: Find student IDs enrolled in exactly two courses
#
# Written by: JiamingYang z5452842
# Date: 2025-04-07
# For COMP2041/9044 用Counter
# ==============================================================================

from collections import Counter

with open("enrollments.txt", "r") as f:
    ## 取第二元素: cut -d "|" -f2
    student_ids = [line.strip().split("|")[1] for line in f if "|" in line]

# 统计每个 student ID 出现次数
#Counter(list) treats each element in the list as a key in a dictionary, 
#and the corresponding value is the number of times that element appears in the list.
counts = Counter(student_ids)

# 打印只出现 2 次的 ID
for student_id, count in counts.items(): #dict_items 类型 dict_items([('a', 2), ('b', 1)])
    if count == 2:
        print(student_id)