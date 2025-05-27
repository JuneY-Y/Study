#!/usr/bin/env python3
import sys
import re
#handle read all lines
# lines=sys.stdin.readlines()
file=sys.argv[1]
with open (file,'r')as f:
    for line in f:
        if re.findall(r'^[0-9]+/.[0-9]+',line):
            print(line)