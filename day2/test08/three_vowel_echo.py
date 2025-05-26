#!/usr/bin/env python3
import sys
import re


for word in sys.argv[1:]:
    if re.findall(r'[AEIOUaeiou]{3}',word):
        print(word, end=' ') #符合条件的单词用空格拼接，不换行

print()
