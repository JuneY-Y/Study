#!/usr/bin/env python3

'''
grep -E '\|M$'|cut -d '|' -f3|cut -d "," -f1|tr -d ' '|sort|uniq
'''
import sys
file=sys.argv[1]
# with open (file,'r') as f: 🌟 in comand   #./practice_q3.py enrollments.txt
    # lines=f.readlines() ## readlines is a funciton

lines=[line.rstrip("\n") for line in sys.stdin]

print(lines)