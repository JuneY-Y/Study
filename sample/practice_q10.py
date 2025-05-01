#!/usr/bin/env python3

## 考察了Counter内容，以及if+for用法(这个我还是非常熟练的)
#counter需要继续复习，这个我认为难易程度：简单
#这个是没有想到的: set(...)：如果所有字符出现次数一样，那 set 只有 1 个元素
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
