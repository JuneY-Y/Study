#!/bin/dash

## 用flag判断 missing number
## 读取文件

# bolloon flag="flase"
filename=$1

numbers=$(cat $filename| sort|uniq|sed 's/ /\\n/g')
# echo $numbers
for num in $numbers; do :
    # echo $num
done

min=$(echo $numbers|head -n1)
max=$(echo $numbers|tail -n1)
echo $min
# echo $max