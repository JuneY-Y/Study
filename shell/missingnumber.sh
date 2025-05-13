#!/bin/dash

filename=$1

n=$(cat $filename|head -n1)
echo "$n"
m=$(cat $filename|tail -n1)
echo "$m"
expect_num=$(((m-n+1)*(m-n)/2))
echo "$expect_num"
total=0

for num in $n; do  ##这里直接for loop了$n中文档的数字个数
    echo num
    echo "$num"
    total=$((total+num))
done

missingnumber=$((expect_num-total))
if [ $missingnumber -ne 0 ]; then
    echo $missingnumber
fi
