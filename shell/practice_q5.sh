#!/bin/dash
## Find Years an Award Was Not Given
# -ne是数字比较 
#这道题遇到了3处问题，建议重新写一遍🌟 这里在award_q5有重写
# test: ./practice_q5.sh 'Nobel Prize for physics' awards.psv

award=$1
filename=$2
real_award=$(cut -d '|' -f1 $filename)

if ! echo "$real_award"|grep -qE "^$award$";then  ##先写出来真实存在的，再grep设想存在的
    echo "practice_q5.sh: no awards match '"$award"'"
    exit 0
fi

# echo "$real_award"
# for awards in $award;do
years=$(grep -E "^$award\|" "$filename"| cut -d '|' -f2,2|sort -n|uniq) ## 变量名不能写错，而且对于有空格的变量名尤其注意
# echo "$years"
start=$(echo "$years"|head -n1)
end=$(echo "$years"|tail -n1)
# echo "$start"
start_count=$start
# 若为空，直接退出  🌟避免空数据导致 [: -le: argument expected 错误。
if [ -z "$start" ] || [ -z "$end" ]; then
    exit 0
fi

while [ $start_count -le $end ]; do
    if ! echo "$years"| grep -qE "^$start_count$" ;then
        echo "$start_count"
    fi
    start_count=$((start_count+1))
done
# done