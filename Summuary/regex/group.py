import re
m = re.search(r'.*([aeiou]).*([aeiou]).*', 'abcde')
print(m.group(0))
print(m.group(1))
print(m.group(2))