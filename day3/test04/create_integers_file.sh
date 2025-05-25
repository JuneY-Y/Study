#!/bin/dash
## 用到了重定向，其实还是需要慢慢调试一下，不过这个原理和思路都记住就好了
start=$1
end=$2
file=$3

# seq "$start" "$end" > "$3"
count=$start
while [ "$count" -le "$end" ]; do
    # echo "$count"
    echo "$count">>"$3"
    count=$((count+1))
done