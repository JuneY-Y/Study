#!/bin/dash

dir1="$1"
dir2="$2"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <dir1> <dir2>"
    echo "must be two directory"
    exit 1
fi

##check arguments are empty 
#-z = “zero-length”

## 🌟优化
if [ -z "$dir1" ]; then
    echo "dir1 is an empty strings"
    empty_flag=1
fi

if [ -z "$dir2" ]; then
    echo "dir2 is an empty strings"
    empty_flag=1
fi

if [ "$empty_flag" -eq 1 ]; then
    exit 1
fi

## check directories
if [ ! -d "$dir1" ]; then
    echo "$dir1 is not a valid directory"
    exit 1
fi

if [ ! -d "$dir2" ]; then
    echo "$dir2 is not a valid directory"
    exit 1
fi

# check all and test 

for file1 in "$dir1"/*  ##整个directory下的所有文件 "$dir1"/*
do
    file_name=$(basename "$file1")
    # echo "$file_name"
    file2="$dir2/$file_name"
    #echo "$file2"

    if [ -e "$file2" ]; then ## 判断$dir2 是否在同一个目录里
    # '''
    # •	diff：比较两个文件内容
	# •	-i：忽略大小写（例如 A 和 a 视为一样）
	# •	-w：忽略所有空格（包括行末空格、缩进）
	# •	> /dev/null：不显示 diff 输出结果，只通过返回值判断是否相同
	# •	相同返回值为 0，即会进入 then 分支
	# •	不同返回值为非0
    # '''
        if diff -i -w "$file1" "$file2" >/dev/null; then 
            echo "$file_name" 
        fi
    fi
done