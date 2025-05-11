#!/bin/dash

#@ this is the script for extract data

course_code="$1"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <course code>"
    exit 1
fi

if ! echo "$course_code" | grep -qE "^"