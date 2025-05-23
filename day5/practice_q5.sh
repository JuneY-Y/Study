#!/bin/dash

award=$1
file=$2

year=$(grep -E "$1" $2|cut -d '|' -f2|sort|uniq)
echo "$year"