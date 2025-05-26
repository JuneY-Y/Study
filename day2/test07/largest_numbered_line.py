#!/usr/bin/env python3
#!/usr/bin/env python3
import re
import sys

for line in sys.stdin:
    # for lines in line:
    lines=line.strip()
    number=re.findall(r'[0-9]+.[0-9]*',lines)
    # print(number)
    # exit(0)
    for num in range(int(number)):
        print(num)