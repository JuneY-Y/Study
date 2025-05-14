#!/bin/dash

award_name=$1
filename=$2

years= $(grep -E "$award_name" "$filename"|cut -d '|' -f2,2 )