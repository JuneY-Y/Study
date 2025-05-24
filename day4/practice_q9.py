#!/usr/bin/env python3
## takes two command line argument, a positive integer n and the name of a file.

import sys
n=sys.argv[1]
file=sys.argv[2]

with open (file,'r') as f:
    lines=[line for line in f]

