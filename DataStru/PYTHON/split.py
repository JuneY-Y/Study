#!/usr/bin/env python3
import re

'''
\d  匹配：任何数字字符
\D  匹配：任何非数字字符

\w 匹配： 任何单词字符
\W 匹配： 任何非单词字符

\s 匹配：任何空白字符
\S 匹配： 任何非空白字符

\b :字符边界

\A 匹配字符串的开头
\Z 匹配字符串的结尾
'''

text= "COMP9044"
words= re.split(r"comp+", text)
print(words)

text1 = "Hello, world!"
words = [word for word in re.split(r"\W+", text1) if word] ##\D+
print(words)