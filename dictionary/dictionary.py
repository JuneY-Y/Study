import sys,re
from collections import defaultdict
'''
	•	动物名称中，如果是 复数形式结尾的 s（如 Orcas），请去掉末尾的 s
	•	如果是 以 's 结尾（如 Bryde's whale），保留 's 不做处理
'''
# observations=[]
observations=defaultdict(lambda:{'groups':0, 'total':0}) # 修改为全局变量✅
# pod=0
for filename in sys.argv[1:]:
    with open(filename, "r") as f:
        for line in f:
            words=line.strip().split()
            # groups=words[2]
            # total=words[1]
            if len(words)<3:
                continue ###防止有空行或者格式不符合的行 会导致错误
            try:
                total=int(words[1]) ###words 不能直接参与数量统计，string变为int才可以
            except ValueError:
                continue ##如果words[1]这里不是数字就跳过
            
            raw_name=" ".join(words[2:]) #动物名如何提取加上拼接，✅
            name=raw_name.lower() ## 这里调整了顺序，先拼接然后再一个一个对于有“s”的归一化
            defaultdict(lambda: {'groups':0, 'total':0})
            if(words.lower(),endswith("s") and not endswith("'s")): ##这里判断如果是s，那么去掉s

                Modify_w=words.del(1)## 如果是那就删除最后一个s，只删除是复数的
                observations= " ".join(Modify_w) ## 归一化的词输出为物种名称
                
            sorted(dict.keys()) ##这里你提供给我了，但是我不知道怎么用。
print(f"{observations} observations: {pod} pods, {total} individuals")

