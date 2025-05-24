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
        freq_set=set(char_count.values())