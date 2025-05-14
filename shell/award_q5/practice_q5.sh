#!/bin/dash
# check filed以后不要慌，需要检查一下就好
award_name=$1
filename=$2

#years=$(grep -E "^$1\|" "$2" | sort -t'|' -k2 | cut -d'|' -f2)
years=$(grep -E "^$award_name\|" "$filename"|cut -d '|' -f2|sort |uniq ) ##需要检查synatx
# echo "$years"
if [ -z "$years" ]; then ## 不止1年的year，所以需要“”
    echo "No award matching '$award_name'"
    exit 0
fi

start_year=$(echo "$years"|head -n1)
# echo "$start_year"
end_year=$(echo "$years"|tail -n1)
# echo "$end_year"
count=$start_year
while [ "$count" -le "$end_year" ];do
    if ! echo "$years"|grep -Eq "^$count$"; then ##如果都输出了，检查下grep -Eq
        echo "$count"
    fi
    count=$((count+1)) ##这里这样写没有影响
done
# #!/bin/dash

# award_name=$1
# filename=$2

# # years=$(grep -E "^$1\|" "$2" | sort -t'|' -k2 | cut -d'|' -f2)
# years=$(grep -E "^$award_name\|" "$filename"|cut -d '|' -f2|sort |uniq ) ##需要检查synatx
# # echo "$years"
# if [ -z "$years" ];then ## 不止1年的year，所以需要“”
#     echo "No award matching "$years""
#     exit 1
# fi

# start_year=$(echo "$years"|head -n1)
# # echo "$start_year"
# end_year=$(echo "$years"|tail -n1)
# # echo "$end_year"
# count=$start_year
# while [ $count -le $end_year ];do
#     if ! echo "$years"|grep -Eoq $count; then ##如果都输出了，检查下grep -q
#         echo "$count"
#     fi
#     count=$(( $count+1 ))
# done