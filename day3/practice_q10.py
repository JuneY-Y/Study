#!/usr/bin/env python3

import sys
from collections import Counter


# file=sys.argv[1]
for lines in sys.stdin:
    line=lines.strip()
    words=line.split()
    balance=[] ## 放在这里，可以根据每行line进行处理并且自动换行，当在for line这个forloop外面是只打印一行
    for word in words:
        word_low=word.lower()
        count=Counter(word_low)
        print(f"the value is :{count.values()}")
        frequency=set(count.values())  #这个用法还会在哪里被用到，一定要记住了 count.values返回什么
        print(f"the fre_word:{frequency}")
        if len(frequency)==1:
            balance.append(word)
    print(' '.join(balance))
    
