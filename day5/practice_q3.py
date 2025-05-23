#!/usr/bin/env python3
import sys
## 用什么写什么。先把名字都放进surname set里面
#set不能直接打印
#🌟 错误点，处理line的时候，首先需要strip()
# grep -E '\|M$'|cut -d '|' -f3|cut -d "," -f1|tr -d ' '|sort|uniq


surnames=set()

for line in sys.stdin: ##默认有\n
    ## 这里需要进行处理
    line=line.strip()
    if line.endswith('|M'):
        part=line.strip().split('|')
        name=part[2]
        surname=name.split(',')[0].strip()
        surnames.add(surname)


for s in sorted(surnames):
    print(s)
# #!/usr/bin/env python3
# import sys

# surnames = set()

# for line in sys.stdin:
#     line=line.strip()

#     if line.endswith('|M'):
#         parts=line.split('|')
#         name=parts[2]
#         surname=name.split(',')[0].strip()
#         surnames.add(surname)

# for s in sorted(surnames):
#     print(s)