#!/bin/dash

cut -d "|" -f2 | sort | uniq -c | grep '^ *2 ' | sed 's/^ *2 //'

# cut -d"|" -f2 enrollments.txt | sort | uniq -c | awk '$1 == 2 {print $2}'

# cut -d"|" -f2 enrollments.txt | sort | uniq -c | grep '^ *2 ' | sed 's/^ *2 //'

#   所以 ^ *2  的意思是：

# 	“这一行的开头，可以是没有空格或者有很多空格（都可以），然后接着是一个数字 2，再后面是空格。”