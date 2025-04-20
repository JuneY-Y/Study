import sys,re
'''
	•	动物名称中，如果是 复数形式结尾的 s（如 Orcas），请去掉末尾的 s
	•	如果是 以 's 结尾（如 Bryde's whale），保留 's 不做处理
'''
observations=[]
pod=0
for filename in sys.argv[1:]:
    with open(filename, "r") as f:
        for line in f:
            words=line.strip().split()
            groups=words[2]
            total=words[1]
            defaultdict(lambda: {'groups':0, 'total':0})
            if(words.lower(),endswith("s") and not endswith("'s")): ##这里判断如果是s，那么去掉s
                Modify_w=words.del(1)## 如果是那就删除最后一个s，只删除是复数的
                observations= " ".join(Modify_w) ## 归一化的词输出为物种名称
                
            sorted(dict.keys()) ##这里你提供给我了，但是我不知道怎么用。
print(f"{observations} observations: {pod} pods, {total} individuals")

