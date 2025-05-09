#!usr/bin/env python3
'''
python3 script.py COMP1511  # 通过
python3 script.py COMP      # 报错：Invalid course code: COMP
python3 script.py           # 报错：Usage: script.py <course code>

exam point
	•	assert 条件, 错误信息：
	•	如果条件为 False，程序会抛出 AssertionError，并输出错误信息
'''
import sys
import re

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]}<course code>")
    sys.exit(1)
course_prefix=sys.argv[1]



# course_prefix= sys.argv[1]
# assert len(sys.argv) == 2, f"Usage: {sys.argv[0]} <course prefix>"
# assert re.fullmatch(r"[A-Z]{4}[0-9]{4}", course_prefix), f"Invalid course code: {course_prefix}"


# print(f"Valid course code: {course_prefix}")