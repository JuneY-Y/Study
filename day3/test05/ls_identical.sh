#!/bin/dash
# ❌ 你在用
#  if [ “$file1” -eq “$file2” ]
# 但是 -eq 只能用于数字比较，不能用于字符串比较！

di1=$1
di2=$2
file=""
for file1 in "$di1"/*; do
    filename1=$(basename "$file1")
    # file1=$(echo "$file1"|cut -d '/' -f2)
    # echo "$file1"
    for file2 in "$di2"/*;do
        filename2=$(basename "$file2")
        # echo "$file2"
        # file2=$(echo "$file2"|cut -d '/' -f2)
        if [ "$filename1" = "$filename2" ];then
            # file=$(echo "$file1"|cut -d '/' -f2)
            if cmp -s "$file1" "$file2";then ##cmp 需要两个文件的完整路径去比较内容。
                file=$filename1
            fi 
        fi
    done
done
echo "$file"
