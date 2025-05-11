#!/usr/bin/env python3
from collections import defaultdict

students=defaultdict(set)


with open("emrollments.txt") as file:
    for line in file:
        parts=line.strip().split('|')
        name=parts[2]
        course=parts[0]
        students[name].add(course)

for name,courses in students.items():
    if len(courses)>=3:
        print(f"{name} - {', '.join(sorted(courses))}")