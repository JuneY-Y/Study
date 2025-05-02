import sys
import re
'''
	•	sys.argv[1]
	•	line.strip().split()
	•	re.findall(r"\d+", line)
	•	条件判断 + 类型转换
'''
with open(sys.argv[1]) as f: ## 如何读多个文件呢？
    for line in f:
        parts=line.strip().split()
        if re.findall(r"\d+", line):  ## 寻找数字 
            print("AllGoods")  ## 这里print如何输出数字呢？
        else:
            print("Nothing at all")