#!/usr/bin/env python3
'''
	•	sys.stdin
	•	collections.Counter
	•	re.findall(...)
	•	.lower()
	•	counter.most_common(3)
'''
import sys, re
from collections import Counter 

count = Counter()
for line in sys.stdin:
    words = re.findall(r"[a-zA-Z]+", line)  # Fix regex to match words 这里忘记[]+，这个+ 匹配更多
    words = (word.lower() for word in words)  # 配合counter使用这个生成表达式，效果更佳
    count.update(words)

# Print the most common words from top 1 to top 3 🌟 这里count.most_common(3) 是新的用法
for rank, (word, freq) in enumerate(count.most_common(3), start=1): ## copilot 写的，写的真是太好了
    # print(f"Top {rank}: {word} ({freq} occurrences)")
    print(f"{word}: {freq}")
