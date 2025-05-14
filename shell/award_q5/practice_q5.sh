#!/bin/dash

award_name=$1
filename=$2

# years=$(grep -E "^$1\|" "$2" | sort -t'|' -k2 | cut -d'|' -f2)
years= $(grep -E "^$award_name\|" "$filename"|cut -d '|' -f2|sort |uniq )
echo "$years"