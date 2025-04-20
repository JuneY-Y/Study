import sys, re
'''
编写一个 Python 脚本，接收一个文本文件作为参数
提取该文件中所有出现的数字（无论在哪里，只要是连续数字串），并输出这些数字的总和。
'''

for filename in sys.argv[1:]:
    with open (filename, "r") as f:
        for line in f:
            num=re.findall(r"\d+", line)

print(f"{sum(num)}")


