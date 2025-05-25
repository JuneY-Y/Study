#!/bin/dash

sort -t'|' -k2,2 |uniq -c -f1|grep -E '^ *2'| tr -s ' '|cut -d '|' -f2