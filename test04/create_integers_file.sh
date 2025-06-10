#!/bin/dash
start=$1
end=$2
filename=$3

i=$start
#count the number between started to ended
while [ "$i" -le $end ]; do
    if [ $i -eq $start ]; then
        echo $i>$filename
    else
    ## 重定向
        echo "$i">>"$filename"
    fi
    i=$((i + 1))
done