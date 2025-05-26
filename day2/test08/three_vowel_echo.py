#!/usr/bin/env python3
import sys
import re


for line in sys.argv[:]:
    vow=re.findall(r'[AEIOUaeiou]{3}',line)
    print(vow) #[]['eii'][]['Aeo'][]
