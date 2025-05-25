#!/usr/bin/env python3

import sys
from collections import Counter

balance=[]
# file=sys.argv[1]
for lines in sys.stdin:
    line=lines.strip()
    words=line.split()
    for word in words:
        word_low=word.lower()
        count=Counter(word_low)
    
