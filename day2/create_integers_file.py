#!/usr/bin/env python3
'''
实现和week test4.1 相同的script function,用py实现
'''
import sys
start= int(sys.argv[1])
end=int(sys.argv[2])
file=sys.argv[3]
count=start
list=[]
while (count<end+1):
        list.append(count)
        count=count+1
       
with open (file, 'w') as f:
        for line in list:
            f.write(str(line)+'\n')

# with open(file, 'w') as f:
#     for i in range(start, end):
#         f.write(str(i) + '\n')