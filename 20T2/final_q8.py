#!/bin/dash

'''
关键词： equi-lettered
	•	单词中 所有字母的出现次数相同（忽略大小写）； // Case should be ignored
	•	若符合条件，保留该词，否则删除；// with the words which are not equi-lettered removed.
	•	每一行输出保留下来的 equi-lettered 单词，单词之间用一个空格分隔。// separated by a single space character
'''
import sys
from collections import Counter

for line in sys.stdin:
    words=line.strip().split()
    result=[]
    for word in words:
        lower_word=word.lower()
        counts=