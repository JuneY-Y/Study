#!/usr/bin/env python3
'''
	•	特殊条件：比如“不超过 n 不用改”“无空格不改”
	•	优先级：比如先按前 n 个找空格，找不到再全行找

'''
import sys
n=int(sys.argv[1])
filename=sys.argv[2]

with open(filename, 'r') as f:
    lines=f.readlines()

new_lines=[]
for line in lines