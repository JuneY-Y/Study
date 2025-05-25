#!/bin/dash
# 这里面sort uniq的考法巧妙的应用了🌟
sort -t'|' -k2,2|uniq -c -f1|grep -E "^ *2"|cut -d '|' -f2