#!/bin/dash

award=$1
file=$2

years=$(grep -E "$award" "$file"|cut -d '|' -f2|sort -n|uniq)
echo "$years"
head=$(echo "$years"|head -n1)
end=$(echo "$years"|tail -n1)
# echo "$head" "$end"
if [ -e "$years" ];then
    echo no matching "$award">&2
    exit 1
fi
count_year=$head
while [ $head -le $end ];do
    
done