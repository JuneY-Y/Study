#!/usr/bin/env python3
# import sys

# n = int(sys.argv[1])
# filename = sys.argv[2]

# with open(filename, 'r') as f:
#     lines = f.readlines()

# new_lines = []
# num=1
# for line in lines:
#     line = line.rstrip('\n')
#     # num=num+1
#     # print(f"{num}: {line}")
#     while len(line) > n:
#         if ' ' not in line:
#             new_lines.append(line)
#             break
#         front = line[:n]
#         if ' ' in front:
#             split_index = front.rfind(' ')
#             new_lines.append(line[:split_index])
#             line = line[split_index + 1:]
#         else:
#             split_index = line.find(' ')
#             new_lines.append(line[:split_index])
#             line = line[split_index + 1:]
#     if len(line) <= n:
#         new_lines.append(line)

# with open(filename, 'w') as f:
#     for l in new_lines:
#         f.write(l + '\n')
#!/usr/bin/env python3
## takes two command line argument, a positive integer n and the name of a file.
'''
🌟 小总结
	•	✅ for line in f → 一行一行读
	•	✅ rstrip() → 去掉右边的空白，包括换行符 \n
	•	✅ 适合处理大文件（不会一次性全部读入内存）
'''
import sys
n=int(sys.argv[1])
file=sys.argv[2]
num=0
with open (file,'r') as f:
    # lines=[line for line in f]
    
    for line in f:
        line=line.rstrip()
        num=num+1
        print(f"{num}: {line}")
new_lines=[]
while len(line) > n:
    if ' ' not in line: #这里用了not in 来进行判断
        new_lines.append(line)
        break
    front=line[:n] #n之前的
    if ' ' in front:
        split_index=front.rfind(' ') #找右面的
        new_lines.append(line[:split_index])
        line=line[split_index+1:]
    else:
        split_index=line.find(' ')
        new_lines.append(line[:split_index])
        line=line[split_index+1:]
if len(line) <= n:
    new_lines.append(line)

with open(file, 'w') as f:
    for l in new_lines:
        f.write(l+'\n')

