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
    
            
                


# --- next version
# #!/usr/bin/env python3
# import sys
# import re

# # 定义数字匹配正则：可带正负号、可有小数点
# pattern = r'[+-]?(?:\d+\.\d+|\d+|\.\d+)'

# for line in sys.stdin:
#     # 用 re.sub 替换行中每个数字
#     def round_number(match):
#         num_str = match.group(0)
#         rounded = str(round(float(num_str)))
#         return rounded

#     new_line = re.sub(pattern, round_number, line)
#     print(new_line, end='')  # line 自带换行符