#!/bin/dash

#If multiple first names are equally most common, 
#you should print the one that is alphabetically first.
grep -E "COMP2041|COMP9044" |cut -d "|" -f2,3|sort -n|uniq|cut -d "," -f2|cut -d ' ' -f2|sort|sed "s/ //"|uniq -c|sort -r|sed 's/^ *//'|cut -d ' ' -f2|head -n1