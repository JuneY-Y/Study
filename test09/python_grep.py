#!/usr/bin/env python3
'''
	•	re.search(…) 是用来匹配正则表达式的。
	•	print(line, end=’’) 避免多加一个换行（因为 line 已经自带换行符）。
'''
import sys
import re
regexexp=sys.argv[1]
file=sys.argv[2]

with open (file, 'r')as f:
    for lines in f:
        if re.search(regexexp,lines): ## = grep 这个是只有这里不大会
            print(lines, end='')
