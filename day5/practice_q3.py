#!/usr/bin/env python3
import sys
## 用什么写什么。先把名字都放进surname set里面
#set不能直接打印
#🌟 错误点，处理line的时候，首先需要strip()
# grep -E '\|M$'|cut -d '|' -f3|cut -d "," -f1|tr -d ' '|sort|uniq
'''
再写个简单的sh和py转换吧，我看这次第一次考试的final题应该是有2个sh和py实现同功能的script，
所以一共是4道题，再加上两个必会的题，就能一下子做出6道了，
离我的目标9道只有三道题，真的很幸福。所以写简单的sh时候，要提醒我用py怎么实现同样的逻辑：
'''
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