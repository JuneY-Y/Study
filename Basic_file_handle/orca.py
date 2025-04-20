## 考点： 读取单个或者多个文件，读取多行，对于行的处理，这道题主要是以计数去考查

'''
	•	sys.argv
	•	with open(...)
	•	line.strip().split()
	•	" ".join(...)
	•	int(...)
'''
import sys, re
count=0 #count 因为要累加，所以写在全局变量
for filename in sys.argv[1:]: ##如果不这么写的话，会报错
# 报错为:  with open(sys.argv[1:], "r") as f:
#          ^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: expected str, bytes or os.PathLike object, not list
    with open(filename, "r") as f:
        for line in f: ## 
            words=line.strip().split() ##这里我需要提取第三行，动物名称。不会写了
            animal_name=" ".join(words[2:])
            if animal_name=="Orca":
                num=int(words[1]) ## 这里出问题了，一定要把它放到另一个容器里
                count=count+num #两个数字进行累加
    
print(f"{count} Orcas reported")

            
        
