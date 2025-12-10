#!/usr/bin/env python3

import sys
from collections import Counter

n = int(sys.argv[1])
counter = Counter()
	# •	统计标准输入（STDIN）中每行文本出现的次数
	# •	当某行文本第 n 次出现时，输出 Snap: 加该行文本
	# •	并立即退出程序

for line in sys.stdin: # stdin? 
    line = line.rstrip('\n') #rstrip
    counter[line] += 1
    if counter[line] == n:
        print("Snap:", line)
        break