#!/usr/bin/env python3

import requests
import bs4
import sys
import re

YEAR = "2024"

# 参数检查
assert len(sys.argv) == 2, f"Usage: {sys.argv[0]} <course prefix>"
course_prefix = sys.argv[1]
assert re.fullmatch(r"[A-Z]{4}", course_prefix), f"Invalid course prefix: {course_prefix}"

# 解析 HTML
url = f"http://www.timetable.unsw.edu.au/{YEAR}/{course_prefix}KENS.html"
soup = bs4.BeautifulSoup(requests.get(url).text, "html5lib")

courses = []

# 遍历所有 <a> 标签
for tag in soup.find_all("a"):
    code = tag.get("href", "")
    name = tag.text.strip()  # 去除前后空格  这里是最后改进的tag不会

    if re.fullmatch(r"[A-Z]{4}[0-9]{4}\.html", code) and code[:-5] != name:
        courses.append((code[:-5], name))

# 去重 & 排序输出
for code, name in sorted(set(courses)):
    print(f"{code} {name}")
# #! /usr/bin/env python3

# import requests
# import bs4
# import sys
# import re

# YEAR="2024"

# assert len(sys.argv)==2, f"Usage:{sys.argv[0]} <course prefix>"
# course_prefix= sys.argv[1]
# assert re.fullmatch(r"[A-Z]{4}", course_prefix), f"Invalid course prefix: {course_prefix}"


# ## 用soup进行解析
# url = f"http://www.timetable.unsw.edu.au/{YEAR}/{course_prefix}KENS.html"
# soup=bs4.BeautifulSoup(requests.get(url).text, "html5lib")

# course=[]
# for tag in soup.find_all("a"):
#     code=tag.get("href", "")
#     name=tag.text

#     if re.fullmatch(r"[A-z]{4}[0-9]{4}\.html", code) and code[-5]!=name: ##code[-5]?在一般语境里指什么
#         courses.append((code[:-5], name))

#         for code, name in sorted(set(courses)):
#             print(f"{code}{name}") ## 如果不加空格会怎么样x


