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
###use sub and counter 
# import sys
# from re import sub
# from collections import Counter

# if len(sys.argv)!=2:
#     print(f"Usage: {argv[0]} <N>")
#     sys.exit(0)

# N=int(sys.argv[1])
# lines=Counter()
# for index, line in enumerate(sys.stdin, 1):
#     line=sub(r"\s", "", line)
#     line=line.lower()
#     lines[line] +=1
#     if len(lines)==N:
#         print(f"{N} distinct lines seen after {index} lines read.")
#         break
# else:
#     print(
#         f"End of input reached after {index} lines read - {N} different lines not seen."
#     )