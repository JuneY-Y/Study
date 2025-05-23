#!/usr/bin/env python3
from collections import defaultdict
# 找出那些注册（enroll）了“三门及以上课程”的学生，并输出这些学生的名字和他们所选的课程。
students=defaultdict(set)


with open("enrollments.txt") as file:
    for line in file:
        parts=line.strip().split('|')
        name=parts[2]
        course=parts[0]
        students[name].add(course)

for name,courses in students.items():
    if len(courses)>=3:
        print(f"{name} - {', '.join(sorted(courses))}") #有序（按字母排序）输出
