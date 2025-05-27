#!/usr/bin/env python3

import sys
import re

for file in sys.stdin:
    lines=file.strip()
    for line in lines:
        if not re.search(r'#\d+',line):
            print(line,end='')
    print('\n')
    # print(lines)
    

    