#!/bin/dash

award=$1
file=$2

years=$(grep -E "^$award\|" "$file"|cut -d '|' -f2|sort -n|uniq) ##regex 通过不了tet4匹配所有是为什么
# echo "$years"

if [ -z "$years" ]; then ## 不止1年的year，所以需要“”
    echo "No award matching '$award'"
    exit 0
fi

head=$(echo "$years"|head -n1)
end=$(echo "$years"|tail -n1)
# echo "$head" "$end"
# if [ -e "$years" ];then
#     echo no matching "$award"
#     exit 1
# fi
count_year=$head
while [ "$count_year" -le "$end" ];do
    if ! echo "$years"|grep -Eq "$count_year";then
        echo "$count_year"
    fi
    count_year=$(( count_year+1 ))
done