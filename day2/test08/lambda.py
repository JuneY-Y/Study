import sys
'''
✅ lines → 文件的每一行
✅ x → lines 里的某一行（带换行符的字符串）
'''
lines=['1','2','3','612']

sorted(lines, key=lambda x: (len(x), x))