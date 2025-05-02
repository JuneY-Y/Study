#!/bin/dash

sum=0
start=1
finish=100

while((i <= finish)); do
    sum= $((sum+i))
    i=$((i+1))
done

echo "$sum"