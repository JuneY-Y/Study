#!/bin/dash

filename= $1

n=$(cat $filename|head -n1)
echo "$n"
m=$(cat $filename|tail -n1)
echo "$m"
expect_num=$(((m-n+1)*(m-n)/2))
echo "$expect_num"
