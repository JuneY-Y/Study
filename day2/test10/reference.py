#!/usr/bin/env python3

import sys
import re

for file in sys.stdin:
    lines=file.strip()
    for line in lines:
        if re.search(r'#[A-Z]',line) not in line:
            print(line)
    # print(lines)
    

    