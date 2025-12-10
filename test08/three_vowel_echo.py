#!/usr/bin/env python3

from sys import argv
from re import search,I

words=[]
for word in argv[1:]:
    if search(r'[aeiou][aeiou][aeiou]', word,flag=I):
        words.append(word.strip())
#输出
print(' '.join(words))

# version2
# import sys
# import re


# for word in sys.argv[1:]:
#     if re.findall(r'[AEIOUaeiou]{3}',word):
#         print(word, end=' ') #符合条件的单词用空格拼接，不换行

# print()
