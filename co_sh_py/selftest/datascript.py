#!/usr/bin/env python3
import sys
import re

course_code=sys.argv[1]

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <course code>")
    sys.exit(1)

if not re.fullmatch(r"[A-Z]{4}[0-9]{4}", course_code):
    print(f"Invalid course code: {course_code}")
    sys.exit(1)

with open("enrollments.txt") as file:
    for line in file:
        if line.startswith(course_code):  ##??? startswith
            parts=line.strip().split('|')
            print(f"{parts[2]} {parts[4]}")
