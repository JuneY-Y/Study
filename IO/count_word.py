#!/usr/bin/env python3

'''
标准输入类型的题目
'''

#用这行命令进行测试 echo "Orca orca Whale ORCA"| python3 count_word.py orca
import sys,re
from collections import Counter
counter= Counter()## 这个直接调用库就好
for words in sys.stdin:
        w = re.findall(r"[a-zA-Z]+", words)
        words = [word.lower() for word in w] ## 这里w是个list类型，✅
        ##转为string，是要对每一个元素进行lower的处理⬆️
        counter.update(words) #Counter()只用来构造 ✅
        ## update是自动 每个类别的词进行更新的 ✅
# ['orca', 'orca', 'whale', 'orca'] occurred Counter({'orca': 3, 'whale': 1}) times


print(f"{target} occurred {counter[target]} times")
# print(f"{words} occurred {counter} times")
    
