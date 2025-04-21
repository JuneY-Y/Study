import sys, re
import glob
from collections import Counter
'''
<出现次数>/<总词数> = <频率> <歌手名>
	•	import glob, os, re
	•	re.findall(r"[a-zA-Z]+", ...)
	•	.lower()
	•	Counter(words)
	•	sum(counter.values()) 计算总词数
	•	count = counter[target] 获取目标词频
'''
# count_words=Counter() 多个result先不用counter
results=[] #多个result是复数
for file in glob.glob("/lyrics *.txt"): ## 需要带“”
    with open(file,"r") as f:
        for word in sys.stdin:
            ##歌手名如何从文件里提取？ argv[-1:] 这样删除吗？


#!/usr/bin/env python3

import sys
import re
import glob
import os
from collections import Counter

# 获取目标单词，并转为小写（不区分大小写）
target = sys.argv[1].lower()

# 保存所有结果：[(artist, count, total), ...]
results = []

# 遍历 lyrics 文件夹下所有歌词文件
for file_path in sorted(glob.glob("lyrics/*.txt")):
    # 提取歌手名，例如 "lyrics/Taylor_Swift.txt" → "Taylor Swift"
    artist = os.path.basename(file_path).replace(".txt", "").replace("_", " ")

    # 读取文件内容并提取所有单词（忽略大小写）
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        words = re.findall(r"[a-zA-Z]+", text)
        words = [w.lower() for w in words]

    # 构建 Counter 来统计词频
    counter = Counter(words)
    total = sum(counter.values())          # 总词数
    count = counter[target]                # 目标词出现次数

    results.append((artist, count, total))

# 排序输出结果（按歌手名排序）
for artist, count, total in sorted(results, key=lambda x: x[0]):
    print(f"{count:4}/{total:6} = {count/total:.6f} {artist}")

    