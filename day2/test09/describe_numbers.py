#!/usr/bin/env python3
'''
The count of how many numbers
The count of how many unique numbers 不同的数字
The minimum number
The maximum number
The mean of the numbers
The median of the numbers
The mode of the numbers = import mul
The sum of the numbers
The product of the numbers 数字的乘积

	•	len()、set()、min()、max()、sum()
	•	reduce()、mul()（算乘积）
	•	statistics.mean、median、mode(统计值)
'''
import sys
from statistics import mean, median,mode
from functools import reduce
# import operator
from operator import mul


numbers=list(map(int,sys.argv[1:])) # 转为整数列表
if not numbers:
    print("Please provide some numbers as arguments")
    sys.exit(1)

count=len(numbers)
unique_count=len(set(numbers))
total=sum(numbers)
product=reduce(mul, numbers, 1)
mini=min(numbers)
maxi=max(numbers)
avg=mean(numbers)  #mean → 平均数（算术平均值
med=median(numbers)
try:
    mod=mode(numbers) ##uniq number
except:
    mod="no unique mode"