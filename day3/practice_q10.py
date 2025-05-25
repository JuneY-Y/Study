#!/usr/bin/env python3

import sys
from collections import Counter
'''
还需要再写一遍，熟悉，能用，出另一道题也能挪用才可以
len(set(votes.values())) == 1:
✅ count.values() → 返回字典里的值（类型是 dict_values，可以当作 list 用）
✅ set(count.values()) → 得到所有不同的出现次数
✅ len(set(...)) → 判断出现次数是否完全一致
'''

# file=sys.argv[1]
for lines in sys.stdin:
    line=lines.strip()
    words=line.split()
    balance=[] ## 放在这里，可以根据每行line进行处理并且自动换行，当在for line这个forloop外面是只打印一行
    for word in words:
        word_low=word.lower()
        count=Counter(word_low)
        # print(f"the value is :{count.values()}")
        #🌟 set去重复值，如果都只出现一次，那么就是单词里的字母都只出现一次
        frequency=set(count.values())  #这个用法还会在哪里被用到，一定要记住了 count.values返回什么
        # print(f"the fre_word:{frequency}")
        if len(frequency)==1:
            balance.append(word)
    print(' '.join(balance))
    
