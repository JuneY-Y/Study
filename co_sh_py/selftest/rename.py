#!/usr/bin/env python3
##  学生重名检查，这个重名检查用到了defaultdict字典，不是很熟悉的
from collections import defaultdict

names=defaultdict(set)
with open("emrollments.txt") as file:
    for line in file:
        parts=line.strip().split('|')
        # parts=line.strip().split('|')
        name=parts[2]
        course=parts[0]
        names[name].add(course)

for name, courses in names.items():
    if len(courses) >1:
        print(f"{name}-{', '.join(sorted(courses))}")