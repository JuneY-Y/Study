#!/usr/bin/env python3

import sys
## use set 
norepeat = set()
for arg in sys.argv[1:]:
    if arg not in norepeat:
        # this end='' is a format to print result match the require
        print(arg, end=' ')
        #set.add()
        norepeat.add(arg)
print()