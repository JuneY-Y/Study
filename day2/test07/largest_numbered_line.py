#!/usr/bin/emv python3

import sys
import re

#读入输入行
lines=sys.stdin.readlines()
#提取数字
numbers=[]
for line in lines:
    num=re.findall(r'[0-9]+.[0-9]+', line)
    float_num=list(map(float,num)) #list(map(x , x))
    numbers.append(float_num)
