#!/bin/dash

filename=$1

numbers=$(cat "$filename"|sort -n)
echo $numbers