#!/usr/bin/env python3
'''
map(func, iterable)
→ 把 func 应用到 iterable 里的每个元素上，返回一个可迭代对象。
'''
#iterable
nums = [1, 2, 3]
squared = map(lambda x: x * x, nums)
print(list(squared))  # [1, 4, 9]