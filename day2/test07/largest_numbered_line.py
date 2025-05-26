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
#每行最大值
Max=[]
for list in numbers:
    try:
        max=max(list)
        Max.append(max)
    except ValueError:
        pass  ##这一行没有数字，那么跳过

#所有行中最大值
try:
    all_max=max(Max)
    #这个最大值所在的行
    for idx,list in enumerate(numbers):
        if all_max in list:
            print(lines[idx],end='')

except ValueError:
    pass