#!/usr/bin/env python3

#Counter 和 set 联合使用技巧
import sys
from collections import Counter

for line in sys.stdin:
    words=line.strip().split()
    balanced_words=[]
    for word in words:
        lower_word=word.lower()
        char_count=Counter(lower_word)
        freq_set=set(char_count.values()) ##这里是精髓
        if len(freq_set)==1:
            balanced_words.append(word)
    print(' '.join(balanced_words))

from collections import Counter

# c = Counter('banana')
# print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})
# print(c.values())  # dict_values([1, 3, 2])