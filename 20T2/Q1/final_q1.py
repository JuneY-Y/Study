#!/usr/bin/env python3

import sys
result=set()
for line in sys.stdin:
    values=line.split('|')
    zid=values[1]
    names=values[2].split(',')
    first_name=names[1].split()[0] ## ['Kevin', 'Augustus']