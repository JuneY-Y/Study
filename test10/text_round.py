#!/usr/bin/env python3
'''
小数处理部分，只匹配小数： \d+\.\d+
值得学习的点： 正则

'''
import sys
import re
#handle read all lines
lines=sys.stdin.readlines()
for line in lines:
    if num:=re.findall(r'[+-]?(?:[0-9]+\.?[0-9]*|\.[0-9]+)',line): #grep出行里所有数字
        for number in num:
            line =line.replace(number, str(int(float(number) + 0.5))) #把行里找到的数字，转 float，加 0.5，取整（四舍五入），变字符串，换回去。
        print(line, end='')
    else:
        print(line, end='')
# #!/usr/bin/env python3

# import sys
# import re  # Import regular expression module

# # Loop through each line of standard input
# for line in sys.stdin:
#     # Find all floating point numbers in the line using regex: (\d+\.\d+)
#     numbers = re.findall(r'(\d+\.\d+)', line)

#     # For each number found, round it to the nearest integer
#     for number in numbers:
#         # Replace the original number with the rounded version
#         # float(number) + 0.5 simulates rounding
#         line = line.replace(number, str(int(float(number) + 0.5)))

#     # Print the modified line (suppressing extra newline from print)
#     print(line, end='')