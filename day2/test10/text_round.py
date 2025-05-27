#!/usr/bin/env python3
import sys
import re
#handle read all lines
lines=sys.stdin.readlines()
for line in lines:
    if m:=re.findall(r'[+-]?(?:[0-9]+\.?[0-9]*|\.[0-9]+)',line):
        print(m)
        if m is float:
            if y.x>5:
                y=y+1
            else:
                y=y-1
            
                


