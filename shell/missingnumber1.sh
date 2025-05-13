#!/bin/dash

## 先不用flag 用python里的for n not in m
## 用flag判断 missing number
## 读取文件

# bolloon flag="flase"
filename=$1

numbers=$(cat "$filename"| sort -n)
# echo $numbers
# for num in $numbers; do :
#     # echo $num
# done

min=$(echo "$numbers"|head -n1) # "$numbers"
max=$(echo "$numbers"|tail -n1)
# echo $min,$max
