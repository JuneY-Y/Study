import sys
'''
✅ lines → 文件的每一行
✅ x → lines 里的某一行（带换行符的字符串）
'''
lines = ['apple', 'dog', 'banana']
#             key: 对列表中每个元素生成一个“排序用权重”
sorted(lines, key=lambda x: (len(x), x))

# 对于每个行 x，
# 生成一个排序用的“权重” → 一个元组 (行的长度, 行的内容本身)
	# •	先按 len(x) 排序（数字）
	# •	如果长度相同，再按 x 排序（字母序）
lambda x: (len(x), x)

#or key: 对列表中每个元素生成一个“排序用权重”
def sort_key(x):
    return (len(x), x)

sorted_lines = sorted(lines, key=sort_key)
### summary
sorted(lines, key=lambda i: len(i))  # 按长度排序
sorted(lines, key=lambda i: i)       # 按字母排序