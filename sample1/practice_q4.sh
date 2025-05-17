#/bin/dash

## 有些地方比如 while [ ]
##又比如 ! 这样的一个逻辑忘掉了
# 🤔需要搞清楚() 和[]的区别是什么
file=$1

# for lines in "$file";do
#     line=(r"$line|sort -n")
# done

numbers=$(cat "$file"| sort -n)
start=$(echo "$numbers"|head -n1)
end=$(echo "$numbers"|tail -n1)
# echo "$numbers" "$start" "$end"
count=$start

while [ "$count" -le "$end" ] ;do
    if ! echo "$numbers" | grep -Eq "$count"; then
        echo "$count"
    fi
    count=$((count+1))
done