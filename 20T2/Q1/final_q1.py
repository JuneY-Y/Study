#!/usr/bin/env python3
import sys
result=set()
for line in sys.stdin:
    values = line.split('|')
    zid = values[1]
    names = values[2].split(',')
    first_name = names[1].split()[0]  # 提取名
    result.add((zid, first_name))     # 保证 zID 唯一地对应一个名

# 只保留名字并排序
result = [name for zid, name in result]
for name in sorted(result):
    print(name)