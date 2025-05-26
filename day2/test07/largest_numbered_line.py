#!/usr/bin/env python3
#!/usr/bin/env python3
import re
import sys
save=[]
for line in sys.stdin:
    for lines in line:
        lines=lines.strip()
        number=re.fullmatch(r'/d',lines)
        print(number)
        # for num in range(int(number)):
        #     print(num)