#!/usr/bin/env python3

import sys, re  # Import system module for stdin, and re module for regular expressions

# Read all input lines from standard input into a list (each line includes a trailing '\n')
lines = sys.stdin.readlines()

# Loop through each line
for line in lines:
    # If the line ends with a newline character, remove it for clean matching
    if line[-1] == '\n':
        line = line[:-1]

    # Check if the line exactly matches the pattern "#<number>" (e.g., "#2", "#7")
    if m := re.fullmatch(r'#(\d+)', line):
        # Extract the number and convert it to int
        line_number = int(m.group(1))
        # Print the referenced line (n-th line); since it already has a newline, use end=''
        print(lines[line_number - 1], end='')

    else:
        # If it's a regular line, print it as-is
        print(line)


# #!/usr/bin/env python3

# import sys, re  # 导入标准输入输出模块和正则模块

# # 从标准输入一次性读取所有行，存入列表，每个元素代表一行（包含换行符 \n）
# lines = sys.stdin.readlines()

# # 遍历每一行内容进行处理
# for line in lines:
#     # 如果该行以换行符结尾，先去掉末尾的 \n，避免影响匹配
#     if line[-1] == '\n':
#         line = line[:-1]

#     # 如果整行完全匹配 #<数字>（例如 #2、#7）
#     if m := re.fullmatch(r'#(\d)', line):
#         # 提取数字部分，转换为 int，用来索引第几行（注意从1开始，所以减1）
#         line_number = int(m.group(1))
#         # 打印引用的那一行内容，原本就包含 \n，所以不需要 print 默认的换行
#         print(lines[line_number - 1], end='')

#     else:
#         # 如果不是 #数字 的形式，原样打印该行
#         print(line)