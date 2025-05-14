#!/bin/dash
# Sequence Generator by Replacing Integer in a String
string1=$1
string2=$2
# echo "$string"
n=$(echo "$string1"| grep -Eo "[0-9]+")
# echo "$n"
m=$(echo "$string2"| grep -Eo "[0-9]+")
# echo "$m"
star_char=$(echo "$string1"|grep -Eo "^[A-Za-z]+") ##正则的时候，直接匹配到行首和行尾符号即可
end_char=$(echo "$string2"|grep -Eo "[A-Za-z]+$")
# echo "$star_char"
# echo "$end_char"
count_num=$n
while [ $count_num -le $m ]; do
    # echo "$count_num"
    echo "$star_char""$count_num""$end_char"
    
    count_num=$(( count_num+1 ))
    # echo $count_num
done
# echo $count_num