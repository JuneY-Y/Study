#!/bin/dash


grep -E "^COMP(2041|9044)" \
| cut -d '|' -f3 \
| cut -d ',' -f2 \
| cut -d ' ' -f2 \
| sort \
| uniq -c \
| tr -s ' ' \
| sort -t ' ' -k2,2nr -k3,3 \  # 先按出现次数降序，再按名字升序排序
| head -n1 \
| cut -d' ' -f3

#awk '$2 ~ /COMP2041|COMP9044/ {print $1}' | sort | uniq -c | sort -k1nr,1 -k2,2 | awk 'NR==1 {print $2}'