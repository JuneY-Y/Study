#!/usr/bin/env python3

import sys
n=int(sys.argv[1])
file=sys.argv[2]

with open (file, 'r') as f:
    for line in f:
        for i in line:
            print(line)
    # for n in range(lines):
    #     print()