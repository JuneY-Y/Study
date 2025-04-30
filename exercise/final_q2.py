#!/usr/bin/env python3

import sys

names_seen = set()      # 用来“去重”——防止重复
first_names = []        # 用来“收集”所有 first name，可能有重复，需要排序

for line in sys.stdin: #sys.stdin
    parts = line.strip().split('|')
    if len(parts)<3:
        continue
    student_id = parts[1].strip()
    full_name = parts[2].strip()

    key = f"{student_id}|{full_name}"
    if key in names_seen:
        continue
    names_seen.add(key)

    if','in full_name:
        after_comma = full_name.split(',')[1].strip()
        first_name = after_comma.split()[0]
        first_names.append(first_name)

for name in sorted(first_names):
    print(name)
