#!/usr/bin/env python3

import sys
orfile=sys.argv[1]
newfile=sys.argv[2]

with open(orfile ,'r') as f1:
    lines=f1.readlines()
    # for line in f1: #一行的字符反转 比如第一行42，变为24
    #     re=list(reversed(line))
    #     print(re)


with open(newfile,'w') as f2:
     for line in reversed(lines):
        f2.write(line)
