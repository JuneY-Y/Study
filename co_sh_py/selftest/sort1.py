#!/usr/bin/env python3

courses=set()
with open ("enrollments.txt") as f:
    for line in f:
        course=line.strip().split('|')[0] ### split是需要('|') 这样进行的，而且需[0]
        # print(course)
        courses.add(course)
print(sorted(courses))
for course_code in sorted(courses):
    print(course_code)

        
    
