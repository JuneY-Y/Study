#!/usr/bin/env python3
import sys
file=sys.argv[1]
with open (file, 'r') as f:
    line=f.readlines() #readlines() 会自动把每一行，包括结尾 \n，作为独立字符串读进列表