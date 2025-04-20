import sys, re
'''
🌟 list初始化
🌟用extend进行insert element
🌟sum() 只能接受int
🌟map还是不是很懂
	•	sys.argv[1]
	•	with open(...) as f
	•	re.findall(r"\d+", ...)
	•	int() + sum(...)
编写一个 Python 脚本，接收一个文本文件作为参数
提取该文件中所有出现的数字（无论在哪里，只要是连续数字串），并输出这些数字的总和。
with open(sys.argv[1]) as f:
    text = f.read()  ##??????? f.read() 应该是另一种写法
numbers = map(int, re.findall(r"\d+", text))
print(sum(numbers))
'''
sums_up = []
for filename in sys.argv[1:]:
    with open(filename, "r") as f:
        for line in f:
            num = re.findall(r"\d+", line)
            sums_up.extend(map(int, num))  # Convert strings to integers and extend the list
print(sum(sums_up))  # Print the sum of all numbers in the list

