#!/bin/dash


sort -t'|' -k2,2 |uniq -c -f1|grep -E '^ *2'| tr -s ' '|cut -d '|' -f2
#  sort -t'|' -k2,2 | uniq -c -f1| grep -E '^ *2'|tr -s ' '|cut -d '|' -f2


# awk '{print $1}' \
# | sort \| uniq -c \| awk "$1 == 2 {print $2}" \| sort -n

# sort -t'|' -k2,2 \
# | uniq -c -f1 \
# | grep -E '^ *2' \
# | cut -d'|' -f2 \
# | cut -d' ' -f2
