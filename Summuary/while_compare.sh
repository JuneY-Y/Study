#!/bin/dash

while true
do
    if diff -q dirA/a.txt dirB/a.txt > /dev/null;then
        echo 'is same'
    else
        exit 0
    fi
done