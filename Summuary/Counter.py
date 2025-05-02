import sys, re
from collections import Counter

counter = Counter()
for line in sys.stdin:  ## 读取terminal的标准输入
    words=re.findall(r"[a-zA-Z]+", line) # re.findall(r"regex", line)
    words=[w.lower() for w in words] # for w in words , w应该是直接在这里就定义好了
    counter.update(words)
print(counter) 
'''
terminal: echo "Orca orca Whale whale WHALE" | python3 Counter.py
Counter({'whale': 3, 'orca': 2})
'''
print(f"{sum(counter.values())} words")