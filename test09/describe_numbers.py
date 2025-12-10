#!/usr/bin/env python3

# 导入命令行参数模块
from sys import argv

# 从 statistics 模块导入统计函数：
# - mean(): 平均值
# - median(): 中位数
# - mode(): 众数（出现次数最多的值）
from statistics import mean, median, mode

# 从 itertools 模块导入 accumulate()，用于累积计算
from itertools import accumulate

# 从 operator 模块导入乘法函数 mul（multiply），配合 accumulate 做乘积
from operator import mul

# 列表推导式：从命令行参数的第2个开始（即 index=1 之后的全部），逐个转成整数
# argv[1:] 是跳过脚本名 argv[0]，只处理后续输入的数字参数
numbers = [int(e) for e in argv[1:]]

# 如果用户有输入数字：
if numbers:
    print(f"count={len(numbers)}")  # 元素总个数
    print(f"unique={len(set(numbers))}")  
    # set(numbers)：去除重复值后的集合，len() 就是唯一元素个数
    
    print(f"minimum={min(numbers)}")  # 最小值
    print(f"maximum={max(numbers)}")  # 最大值

    print(f"mean={mean(numbers)}")     # 平均值
    print(f"median={median(numbers)}") # 中位数
    print(f"mode={mode(numbers)}")     # 众数（最常见的数）

    print(f"sum={sum(numbers)}")  # 总和

    # 计算累积乘积，如 [2, 3, 4] → [2, 6, 24]
    product = list(accumulate(numbers, func=mul))

    print(f"product={product[-1]}")  # 最后一个就是全部乘起来的结果