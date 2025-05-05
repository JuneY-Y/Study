#!/usr/bin/env python3
import sys
from collections import Counter

names = []

for line in sys.stdin:
    line = line.strip()
    if line.startswith("COMP2041") or line.startswith("COMP9044"):
        try:
            # 1. 取出姓名字段（第3列）
            name_field = line.split('|')[2]

            # 2. 拆分成 Last, First
            last_first = name_field.split(',')

            if len(last_first) >= 2:
                first_full = last_first[1].strip()

                # 3. 从 " John Doe" 中取 "John"
                first_name_parts = first_full.split()
                if len(first_name_parts) >= 1:
                    first_name = first_name_parts[0]
                    names.append(first_name)
        except IndexError:
            continue  # 忽略格式错误行

# 4. 统计出现次数
name_counts = Counter(names)

# 5. 按频率降序，名字升序排序
sorted_names = sorted(name_counts.items(), key=lambda x: (-x[1], x[0]))

# 6. 输出第一名
if sorted_names:
    print(sorted_names[0][0])