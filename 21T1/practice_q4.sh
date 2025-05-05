#!/bin/dash

s1=$1
s2=$2

# 提取数字部分
num1=$(echo "$s1" | grep -Eo '[0-9]+')
num2=$(echo "$s2" | grep -Eo '[0-9]+')

# 提取前缀（非数字部分）
prefix=$(echo "$s1" | sed "s/[0-9].*//")
# 提取后缀（从数字结尾到结尾的部分）
suffix=$(echo "$s1" | sed "s/.*[0-9]//")

current=$num1

while [ "$current" -le "$num2" ]; do
    echo "${prefix}${current}${suffix}"
    current=$((current + 1))
done