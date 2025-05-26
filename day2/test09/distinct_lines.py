#!/usr/bin/env python3

import sys
from statistics import mode
N=int(sys.argv[1])
list=[]
count=0
for lines in sys.stdin:
    lines=lines.strip()
    list.append(lines)
    count=count+1
    if N==list[N-1]:
        print(f"{N} distinct lines seen after {count} lines read.")
        exit(0)



mod=mode(list) ##uniq number