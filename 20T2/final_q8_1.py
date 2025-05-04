#!/usr/bin/env python3

# 记录下 第八题还是有错误。会重新练习
import sys
from collections import Counter

for line in sys.stdin:
    words=line.strip().split()
    result=[]
    for word in words:
        lower_word=word.lower() ##
        count=Counter(lower_word)
        freq=set(count.values())
        if len(freq)==1:
            result.append(word)
    print(" ".join(result))
