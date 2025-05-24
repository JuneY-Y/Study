#!/usr/bin/env python3

'''
grep -E '\|M$'|cut -d '|' -f3|cut -d "," -f1|tr -d ' '|sort|uniq
'''
import sys
surnames=set()

# with open (file,'r') as f: 🌟 in comand   #./practice_q3.py enrollments.txt
    # lines=f.readlines() ## readlines is a funciton
for line in sys.stdin:
    line=line.strip()
    if line.endswith('|M'): #如果不输出多看看正则
        part=line.strip().split('|')
        name=part[2]
        surname=name.split(',')
        surname=surname[0].strip()
        surnames.add(surname)

for print_name in sorted(surnames):
    print(print_name)




