import sys,re
from collections import defaultdict
'''
	•	动物名称中，如果是 复数形式结尾的 s（如 Orcas），请去掉末尾的 s
	•	如果是 以 's 结尾（如 Bryde's whale），保留 's 不做处理
'''
# observations=[]
observations=defaultdict(lambda:{'groups':0, 'total':0}) # 修改为全局变量✅ 这里直接自动归类判断了
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
            
            if name.endswith("s") and not name.endswith("'s"):
                name=name[:-1] ### 🌟居然用这种方法去掉了s
            ## 这里直接进行for循环里的累积
            observations[name]['groups'] += 1
            observations[name]['total'] += total
                
            # sorted(dict.keys()) ##这里你提供给我了，但是我不知道怎么用。 ###真就在最后用到了
for name in sorted(observations.keys()): ##这里的官方文档需要查一下
    pod=observations[name]['groups']
    total=observations[name]['total']

    print(f"{name} observations: {pod} pods, {total} individuals")

