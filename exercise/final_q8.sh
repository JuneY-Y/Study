#!/usr/bin/env python3
# ==============================================================================
# File: final_q8.py
# Aim: Print only equi-lettered words from stdin, space-separated
# ------------------------------------------------------------------------------
# A word is equi-lettered if all characters in it occur the same number of times
# (e.g. "Gaga" is equi-lettered, "gauge" is not)
# ==============================================================================

import sys
from collections import Counter

# 判断一个单词是否为 equi-lettered
def is_equi_lettered(word):
    word = word.lower()  # 不区分大小写
    char_counts = Counter(word)  # 统计每个字符出现次数
    count_values = list(char_counts.values())  # 取出所有计数值
    return len(set(count_values)) == 1  # 如果所有值都一样，则是 equi-lettered

# 用于存储符合条件的单词
equi_words = []

# 从标准输入读取每一行
for line in sys.stdin:
    words = line.split()  # 按空格拆分为单词
    for word in words:
        if is_equi_lettered(word):
            equi_words.append(word)

# 输出符合条件的所有单词，空格分隔
print(" ".join(equi_words))