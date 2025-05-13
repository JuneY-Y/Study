#!/bin/dash

filename=$1

numbers=$(cat "$filename" | sort -n)

min=$(echo "$numbers" | head -n1)
max=$(echo "$numbers" | tail -n1)

total1=$(((max - min + 1) * (min + max) / 2))
total_actual=0
for num in $numbers; do
    total_actual=$((total_actual + num))
done

missing=$((total1 - total_actual))

if [ $missing -ne 0 ]; then
    echo $missing
else
    echo "nothing"
fi
# #!/bin/dash

# filename=$1

# number=$(cat $filename|sort -n)
# # echo "$number"
# n=$(echo "$number"|head -n1)
# # echo "$n"
# m=$(echo "$number"|tail -n1)
# # echo "$m"
# expect_num=$(( ( m - n + 1) * ( m + n )/2 ))
# echo "$expect_num"
# total=0

# for num in $number; do  ##这里直接for loop了$n中文档的数字个数
#     echo flag
#     echo "$num"
#     total=$((total + num))
# done

# echo "$total"
# missingnumber=$((expect_num-total))
# if [ $missingnumber -ne 0 ]; then
#     echo $missingnumber
# fi
