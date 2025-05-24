#!/usr/bin/env python3
import sys

n = int(sys.argv[1])
filename = sys.argv[2]

with open(filename, 'r') as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    line = line.rstrip('\n')
    while len(line) > n:
        if ' ' not in line:
            new_lines.append(line)
            break
        front = line[:n]
        if ' ' in front:
            split_index = front.rfind(' ')
            new_lines.append(line[:split_index])
            line = line[split_index + 1:]
        else:
            split_index = line.find(' ')
            new_lines.append(line[:split_index])
            line = line[split_index + 1:]
    if len(line) <= n:
        new_lines.append(line)

with open(filename, 'w') as f:
    for l in new_lines:
        f.write(l + '\n')
# #!/usr/bin/env python3
# ## takes two command line argument, a positive integer n and the name of a file.

# import sys
# n=int(sys.argv[1])
# file=sys.argv[2]

# with open (file,'r') as f:
#     # lines=[line for line in f]
#     for line in f:
#         line=line.rstrip()
# new_lines=[]
# while len(line) > n:
#     if ' ' not in line: #这里用了not in 来进行判断
#         new_lines.append(line)
#         break
#     front=line[:n] #n之前的
#     if ' ' in front:
#         split_index=front.rfind(' ') #找右面的
#         new_lines.append(line[:split_index])
#         line=line[split_index+1:]
#     else:
#         split_index=line.find(' ')
#         new_lines.append(line[:split_index])
#         line=line[split_index+1:]
# if len(line) <= n:
#     new_lines.append(line)

# with open(file, 'w') as f:
#     for l in new_lines:
#         f.write(l+'\n')

