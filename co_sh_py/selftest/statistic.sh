#!/bin/dash

course_code="$1"
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <coourse code>"
    exit 1
fi

# if ! echo "$course_code" | grep -qE "^[A-Z]{4}[0-9]{4}$"; then
#     echo "Invalid course code: $course_code"
#     exit 1
# fi

if ! echo "$course_code"| grep -qE "^[A-Z]{4}[0-9]{4}$"; then
    echo "Invalid course code: $course_code"
    exit 1
fi

male_count=$(grep "^$course_code|" enrollments.txt | awk -F'|' '$5 == "M"'|wc -l)
female_count=$(grep "^$course_code|" enrollments.txt| awk -F'|' '$5 == "F"'| wc -l)

echo "Male: $male_count"
echo "Female: $female_count"