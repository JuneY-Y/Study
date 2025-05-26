#!/usr/bin/env python3

import sys
from collections import Counter
scan=Counter()
# for i, file in enumerate(sys.argv[+1:]):
#     print(f"{i} {file}")
for i in sys.argv[+1:]:
    scan(i)
print(set(scan))
    
