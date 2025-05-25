#!/bin/dash

n=$1
name=$2

start="1"
while [ $start -le $n ];do
    echo hello "$name" > hello"$start".txt
    start=$((start+1))
done