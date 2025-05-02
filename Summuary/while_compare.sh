#!/bin/dash

while true
do
    if diff -q dirA/a.txt dirB/a.txt > /dev/null;then
        echo 'is same'
        exit 0
    else
        echo 'is not really same'
        exit 0
    fi
done