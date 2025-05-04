#!/usr/bin/env python3

import sys
result=set()
for line in sys.stdin:
    values=line.split('|')
    zid=values[1]
    names=values[2].split(',')
    first_name=names[1].split()[0] ## ['Kevin', 'Augustus']
    result.add((zid, first_name)) ## 添加元组映射

result=[name for zid, name in result]
for name in sorted(result):
    print(name)
