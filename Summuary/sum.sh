#!/bin/dash

sum=0

for n in "$@"
do
    sum=$((sum+n))
    echo "$n"
done
echo "$sum"