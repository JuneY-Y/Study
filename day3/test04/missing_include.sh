#!/bin/dash
file1=$1
file2=$2
##need to for loop all of file
#when file is checked, if include "d.h" not exist d.h in directory. then print it in standout
for f in "$@";do
    while IFS= read -r line;do
        check=$(grep -Eo '"[A-Za-z]*.\.h"')
        
        check_name=$(echo "$check"|sed 's/"//g')
        # echo "$check_name"
        if [ ! -e "$check_name" ];then
            echo ""$check_name" included into a.c does not exist"
        fi
    done < "$file1"
    
done
