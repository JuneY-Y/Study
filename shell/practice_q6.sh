#!/bin/dash
## 得奖最多的国家
filename=$1
country=$(cut -d '|' -f5,5 "$filename"|sort|uniq -c|sort -n|tail -n1)
# echo "$country"
format_country=$(echo "$country"|sed "s/^ *//"|cut -d " " -f2-)
sum=$(echo "$country"|sed "s/^ *//"|cut -d " " -f1)
echo "$format_country": "$sum"
# for countries in "$country";do
#     count=$(echo $country|grep -c "^$countries$"|wc -l)
#     echo "$countries"
# done
