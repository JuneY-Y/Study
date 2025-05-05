#!/bin/dash
start=$1
end=$2
filename=$3

i=$start

while [ "$i" -le $end ]; do
    if [ $i -eq $start ]; then
        echo $i>$filename
    else
        echo "$i">>"$filename"
    fi
    i=$((i + 1))
done