#!/usr/bin/env python3
import sys

lines=sys.stdin.read().splitlines()
lines=list(set(lines)) ##与sort|uniq效果相同
lines.sort(key=str.lower)
# words=[w.lower() for w in lines] ## 不区分大小写

# words.sort() ## shell :sort 按照字母排序

for line in lines:
    print(line)