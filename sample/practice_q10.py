#!/usr/bin/env python3

import sys
from collections import Counter

for line in sys.stdin:
    words=line.strip().split()
    balanced_words=[]
    for word in words:
        lower_word=word.lower()
        char_count= Counter(lower_word) #这里使用了counter来计算每个字符出现的次数
        freq_set=set(char_count.values())
        if len(freq_set) ==1:
            balanced_words.append(word)
    print(' '.join(balanced_words))
