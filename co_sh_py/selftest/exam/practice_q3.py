#!/usr/bin/env python3

'''
grep -iE ".*\|M$" | cut -d'|' -f3,3|cut -d ',' -f1|sort |uniq
'''
import sys
import re

result=set()
# with open ("enrollments.txt") as f:
for line in sys.stdin:
        line=line.strip()
        if re.search(r'\|M$', line,re.IGNORECASE):
            print(line)
            name=line.split('|')[2]
            print(name)
            surname=name.split(',')[0]
            result.add(surname)

for results in sorted(result):
    print(results)
