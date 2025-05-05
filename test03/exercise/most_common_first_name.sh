#!/bin/dash
 
 
 grep -E "^COMP(2041|9044)"| cut -d '|' -f3| cut -d ',' -f2| cut -d ' ' -f2|sort|uniq -c| tr -s ' '|sort -t ' ' -k2,2nr| head -n1| cut -d' ' -f3
# grep -E "^COMP(2041|9044)"| cut -d "|" -f3| cut -d "," -f2| sed -E 's/^ *//' | sort -t ' ' -k1,1r -k2,2 |cut -d ' ' -f1|
# head -n1