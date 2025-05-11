#!/usr/bin/env python3

course_code=set()

with open("enrollments.txt") as file:
    for line in file:
        course_code.add(line.split('|')[0])

for code in sorted(course_code):
    print(code)