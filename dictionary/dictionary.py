import sys,re
'''
	•	动物名称中，如果是 复数形式结尾的 s（如 Orcas），请去掉末尾的 s
	•	如果是 以 's 结尾（如 Bryde's whale），保留 's 不做处理
'''
for filename in sys.argv[1:]:
    with open(filename, "r") as f:
        