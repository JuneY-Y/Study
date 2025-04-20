#!/usr/bin/env python3
import sys

lines=sys.stdin.read().splitlines()
lines=list(set(lines)) ##与sort|uniq效果相同

lines.sort() ## shell :sort

for line in lines:
    print(line)