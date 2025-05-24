#!/usr/bin/env python3
import sys

# 获取命令行参数
n = int(sys.argv[1])         # 最大行长度
filename = sys.argv[2]       # 要处理的文件名

# 读取文件所有行
with open(filename, 'r') as f:
    lines = f.readlines()

# 用来存储处理后的新行
new_lines = []

# 遍历每一行
for line in lines:
    line = line.rstrip('\n')  # 去掉行尾换行符

    while len(line) > n:
        # 如果没有空格，直接整行加入，跳出循环
        if ' ' not in line:
            new_lines.append(line)
            break

        # 查看前 n 个字符里有没有空格（优先按单词分行）
        front = line[:n]
        if ' ' in front:
            # 找到最后一个空格的位置，分割
            split_index = front.rfind(' ')
            new_lines.append(line[:split_index])
            line = line[split_index + 1:]  # 去掉分割掉的部分，继续处理剩下的
        else:
            # 如果前 n 个里没有空格，只能从第一个空格分割（强制分）
            split_index = line.find(' ')
            new_lines.append(line[:split_index])
            line = line[split_index + 1:]

    # 如果最后剩下的部分短于 n，直接加进去
    if len(line) <= n:
        new_lines.append(line)

# 写回文件（覆盖原文件）
with open(filename, 'w') as f:
    for l in new_lines:
        f.write(l + '\n')