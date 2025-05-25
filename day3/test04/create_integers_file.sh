#!/bin/dash
start=$1
end=$2
file=$3

seq "$start" "$end" > "$3"