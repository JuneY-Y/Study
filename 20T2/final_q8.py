#!/usr/bin/env python3

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
        counts=Counter(lower_word)
        freq=set(counts.values())
        #print(freq)
        #将每一行中属于 equi-lettered 的单词保留下来，并用空格连接输出
        if len(freq)==1: #出现次数一致，set=1
            result.append(word)
    #把当前行中符合条件的单词，用空格 ' ' 拼接起来，打印成一整行输出。
    print(" ".join(result))