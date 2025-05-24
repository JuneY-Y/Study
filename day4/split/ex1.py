#!/usr/bin/env python3
import sys

result=[]
for line in sys.stdin:
    line=line.strip()
    if ' ' in line:
        index=line.find(' ')
        left=line[:index]
        right=line[index+1:]
        print(left +','+right)
    else:
        print(f'there are not space in {line}')
#🌟 如果要处理一整段多行输入，还可以把所有拼好的部分用 join 拼起来。
print('\n'.join(result))