#!/bin/dash

course_code=$1

if [ -f "course_code" ]; then :
    echo "doesn't have: <$course_code>"
fi


if [ "$#" -lt 1 ]; then  ## 🌟
    echo "Invalid course code: $0 <argument>"
    exit 1
fi

if echo "$course_code" | grep -E "[A-Z]{4}[0-9]{4}" > /dev/null; then :
else
    echo "Usage: $0 <course code>"
    exit 1
fi
