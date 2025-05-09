#!/bin/dash

course_code=$1

if [ ! -f "course_code" ]; then
    echo "Usage: $0 <course code>"
fi

if [ ! -f "course_code" ]; then
    echo "Invalid course code: <$1>"
fi