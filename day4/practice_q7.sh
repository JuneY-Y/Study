#!/bin/dash

#prints shell commands to add extensions to the filenames.
#stdout 如何在stderr中print？
f=$1
if echo "$f" |grep -Eq "\.";then
    echo "$f" already has an extension
    continue;
fi

