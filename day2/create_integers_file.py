#!/usr/bim/env python3
'''
实现和week test4.1 相同的script function,用py实现
'''
import sys
start= int(sys.argv[1])
end=int(sys.argv[2])
file=sys.argv[3]
count=start
list=[]
with open (file, 'w') as f:
    if (count<end):
        list.append(count)
        count=count+1
        
