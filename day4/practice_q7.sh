#!/bin/dash

#prints shell commands to add extensions to the filenames.
#stdout 如何在stderr中print？
f=$1
if echo "$f" |grep -Eq "\.";then
    echo ""$f" already has an extension"
    continue;
fi

if head -n 1 "$f"|grep -qE "^#!";then
    echo ""$f" does not have a #! line"
    continue;
fi

line1=$((head -n 1 "$f"))

if echo "$line1"|grep -qE "python";then
    ext=".py"
elif echo "$line1"|grep -qE "sh";then
    ext=".sh"
elif echo "$line1"|grep -qE "perl";then
if 


newfile="$f$ext"