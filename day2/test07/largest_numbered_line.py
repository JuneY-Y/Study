#!/usr/bin/env python3
import re
import sys

max_value = None
lines_with_max = []

for line in sys.stdin:
    line = line.rstrip('\n')
    numbers = re.findall(r'-?\d+(?:\.\d+)?', line)  # 改进正则：支持负数和小数
    numbers = [float(num) for num in numbers]

    if numbers:
        line_max = max(numbers)
        if (max_value is None) or (line_max > max_value):
            max_value = line_max
            lines_with_max = [line]  # 新最大，重置列表
        elif line_max == max_value:
            lines_with_max.append(line)  # 相同最大，加入列表

if max_value is not None:
    for l in lines_with_max:
        print(l)
# #!/usr/bin/env python3
# #!/usr/bin/env python3
# import re
# import sys

# lines_with_max=[]
# max_value=None
# for line in sys.stdin:
#     # for lines in line:
#     lines=line.strip()
#     number=re.findall(r'[0-9]+.[0-9]*',lines)
#     # print(number)
#     # exit(0)
#     for num in number:
#         number.append(float(num))
    
#     if number:
#         line_max=max(number)
#         if(max_value is None) or (line_max >max_value):
#             max_value=line_max
#             lines_with_max=[line]

# if max_value is not None:
#     for l in lines_with_max:
#         print(l)