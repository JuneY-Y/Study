#!/usr/bin/env python3

import subprocess
import sys
import re

YEAR="2024"

assert len(sys.argv) == 2,  f"Usage: {sys.argv[0]} <course prefix>" ##?
# sys输入为1个参数
course_prefix = sys.argv[1]
## 参数是否为4个大写的英文字母
assert re.fullmatch(r"[A-Z]{4}", course_prefix), f"Invalid course prefix: {course_prefix}"

# 整个一段是需要构造url请求的
url= f"http://www.timetable.unsw.edu.au/{YEAR}/{course_prefix}KENS.html"
## 这应该是去处理http网址进行分析的
# curl? 
proc = subprocess.run(['curl', '--location', '--silent', url], capture_output=True, text=True)

courses=[]
## 这里用到的re.findall 
for m in re.findall(rf".*{course_prefix}[0-9]{{4}}\.html.*$", proc.stdout, flags=re.MULTILINE):
    m=re.search(r"""<a href="(?P<code>[A-Z]{4}[0-9]{4})\.html">(?P<name>.*?)</a>""", m) ## 看不懂
    if m:
        ## 这里为了干什么
        code=m.group('code')
        name=m.group('name')
        if code != name:
            courses.append((code, name))


for code, name in sorted(set(courses)):
    print(f"{code} {name}")
        

