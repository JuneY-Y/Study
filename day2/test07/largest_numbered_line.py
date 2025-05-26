#!/usr/bin/env python3

import sys
save=[]
for line in sys.stdin:
    for lines in line:
        lines=lines.strip()
        number=lines.find(r'/d',lines)
        print(number)