#!/bin/dash

sum=0
start=1
finish=100
i=$start

while [ "$i" -le "$finish" ]; do  ##表达式出错
    sum=$((sum+i)) #赋值变量没有任何空格
    i=$((i+1))
done

echo "$sum"