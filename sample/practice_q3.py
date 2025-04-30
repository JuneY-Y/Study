#!/usr/bin/env python3
import sys

surnames = set()

for line in sys.stdin:
    line=line.strip()

    if line.endswith('|M'):
        parts=line.split('|')
        name=parts[2]
        surname=name.split(',')[0].strip()
        surnames.add(surname)

for s in sorted(surnames):
    print(s)