#!/bin/dash

#@ this is the script for extract data

course_code="$1"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <course code>"
    exit 1
fi

if ! echo "$course_code" | grep -qE "^[A-Z]{4}[0-9]{4}$"; then
    echo "Invalid course code: $course_code"
    exit 1
fi

## 这里需要提取学生的姓名和性别
grep "^$course_code|" enrollments.txt| awk -F'|' "{print $3, $5}"