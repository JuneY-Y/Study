#!/bin/dash

sort -t"|" -k2,2 -u \
| uniq -c \
| cut -d"|" -f3 \
| cut -d"," -f2 \
| cut -d" " -f1,2 \
| sed 's/, *//' \
| cut -d" " -f2 \
| sort


# sort -t"|" -k2,2 | uniq -c | cut -d"|" -f3 | cut -d"," -f1,2 | cut -d" " -f1,2 |
# sed 's/ ,[[ ]]*/\n/'


#sort -t”|” -k2,2 | uniq -c | cut -d" " -f2
#cut -d'|' -f3 enrollments.txt | sed -E 's/^\s*([^,]+)[[:space:]]*,[[:space:]]*([^[:space:]]+).*/\1\n\2/' | sort
