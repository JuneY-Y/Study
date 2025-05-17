#!/usr/bin/env python3
import sys
import re
'''
grep -E '[\|M]$' | cut -d "|" -f3| cut -d "," -f1|sort |uniq

'''
surnames=set()

for line in sys.stdin:
    line=line.strip()
    if line.endswith("|M"):
        fields=line.split('|')
        if len(fields)>=3:
            name_field=fields[2].strip()
            surname=name_field.split(',')[0].strip()
            surnames.add(surname)

    # limit= re.match(r"\|M$", file)
    # line=limit.expand(limit)
for name in sorted(surnames):
    print(name)
