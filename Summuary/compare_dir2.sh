#!/bin/dash

dir1="$1"
dir2="$2"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <dir2> <dir2>"
    echo "must be two directory"
    exit 1
fi

##check arguments are empty 
#-z = “zero-length”
if [ -z "$dir1" ]; then
    echo "dir1 is an empty strings"
    exit 1
fi

if [ -z "$dir2" ]; then
    echo "dir2 is an empty strings"
    exit 1
fi

## check directories
if [ ! -d "$dir1" ]; then
    echo "$dir1 is not a valid directory"
    exit 1
fi

if [ ! -d "$dir2" ]; then
    echo "$dir2 is not a valid directory"
    exit 1
fi