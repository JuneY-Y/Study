#!/usr/bin/env python3

from sys import argv, stdin
import re

# Step 1: 读取字典文件（每一行是一个合法单词）
dictionary = set()
with open(argv[1]) as file:
    for line in file:
        dictionary.add(line.strip())

# Step 2: 递归展开所有可能的单词组合
def recursion(word, solutions):
    if "(" not in word:
        # 特殊情况处理
        if word == "i" or word in dictionary:
            solutions.append(word)
        elif word.endswith("s") and word[:-1] in dictionary:
            solutions.append(word)
    else:
        pattern = r"\((.*?)\)"
        if m := re.search(pattern, word):
            for s in m.group(1):
                recursion(re.sub(r"\(.*?\)", s, word, count=1), solutions)

# Step 3: 主循环处理输入文本
for line in stdin:
    result = []
    words = line.strip().split()
    for word in words:
        if "(" not in word:
            result.append(word)
            continue

        solutions = []
        recursion(word, solutions)
        if len(solutions) == 1:
            result.append(solutions[0])
        elif len(solutions) > 1:
            result.append("{" + ",".join(solutions) + "}")
        else:
            result.append(word)
    print(" ".join(result))