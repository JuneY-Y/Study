#!/usr/bin/env python3
import sys

seen=set()
N=int(sys.argv[1])
count=0
for lines in sys.stdin:
    normalized=' '.join(lines.strip().lower().split())
    # print(normalized)
    seen.add(normalized)
    count+=1
    
    if len(seen)==N:
        print(f"{N} distinct lines seen after {count} lines read.")
        exit(0)
    
print(f"End of input reached after {count} lines read - {N} different lines not seen.")



# mod=mode(list) ##uniq number这个是不能用的