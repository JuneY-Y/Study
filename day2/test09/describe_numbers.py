#!/usr/bin/env python3
'''
The count of how many numbers
The count of how many unique numbers
The minimum number
The maximum number
The mean of the numbers
The median of the numbers
The mode of the numbers
The sum of the numbers
The product of the numbers

	•	len()、set()、min()、max()、sum()
	•	reduce()、mul()（算乘积）
	•	statistics.mean、median、mode(统计值)
'''
import sys
from statistics import mean, median,mode
from functools import reduce
from operator import mul

numbers=list(map(int,sys.argv[1:]))
if not numbers:
    print("Please provide some numbers as arguments")