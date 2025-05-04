#!/bin/dash

## 主要是
cut -d '|' -f2 | sort | uniq -c | while read count student_id ; do
    if [ "$count" -eq 2 ];then # 一个段落，会有 ";"
        echo "$student_id"
    fi
done 
