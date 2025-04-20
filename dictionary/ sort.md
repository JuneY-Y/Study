
⸻

🔍 1. sorted() 官方文档
	•	📘 官方文档链接：https://docs.python.org/3/library/functions.html#sorted

✅ 官方定义（简化翻译）：

sorted(iterable, *, key=None, reverse=False) → new sorted list

	•	作用：返回一个新的排序后的列表，原数据不变。
	•	默认排序规则：字典序（按字符顺序）
	•	常用参数：
	•	key= 指定排序的依据，比如 key=str.lower 忽略大小写
	•	reverse=True 反向排序

✅ 你的使用场景：

for name in sorted(observations.keys()):

解释：
	•	observations.keys() 是所有动物名称
	•	sorted(...) 会返回一个新的列表，排序后的动物名
	•	for name in ... 遍历排序后的名字，确保输出顺序是从 a 到 z

⸻

🔍 2. defaultdict() 官方文档
	•	📘 官方文档链接：https://docs.python.org/3/library/collections.html#collections.defaultdict

✅ 用法示例：

from collections import defaultdict

dd = defaultdict(lambda: {'groups': 0, 'total': 0})

	•	每次访问一个新 key，lambda 会自动提供一个默认值 {'groups': 0, 'total': 0}，不需要你提前创建。
	•	非常适合用于统计题！

⸻

✅ 你还可以在 Python 交互式中尝试：

>>> sorted(["banana", "Apple", "cherry"])
['Apple', 'banana', 'cherry']
>>> sorted(["banana", "Apple", "cherry"], key=str.lower)
['Apple', 'banana', 'cherry']

可以看出 key=str.lower 会让排序不区分大小写。

⸻

🎯 总结你的学习重点：

技能点	你已掌握情况
defaultdict 初始化 + 自动创建嵌套结构	✅ 已熟练
字符串归一化处理（.lower() + .endswith()）	✅ 写得很好
切片 name[:-1] 去除末尾字符	✅ 灵活使用
排序输出：sorted(dict.keys())	✅ 使用正确，现在也理解它的意义了



⸻

你已经非常接近考试-ready 状态了！
明天我们会让这题“换皮”——例如换动物名判断逻辑、加入某种过滤条件、按数量排序等等。

今晚可以休息下，你练到这已经非常棒 💪
随时回来我都在，你就是9044大佬养成中 ✨