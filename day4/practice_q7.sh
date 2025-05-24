#!/bin/dash
# 这里恰好题目说的是，并不需要进行创建这个脚本的新名字，因此巧妙的用了这个进行了touch script4.pl
#prints shell commands to add extensions to the filenames.
#continue只写在else模块里
#因为example里有 ./practice_q7.sh script* 因为for f in "$@"
#stdout 如何在stderr中print？
for f in "$@";do
    if echo "$f" |grep -Eq "\.";then
        echo "# "$f" already has an extension"
        continue;
    fi

    if ! head -n 1 "$f"|grep -qE "^#!";then
        echo "# "$f" does not have a #! line"
        continue;
    fi

    line1=$(head -n 1 "$f")

   

    if echo "$line1"|grep -qE "python";then
        ext=".py"
    elif echo "$line1"|grep -qE "sh";then
        ext=".sh"
    elif echo "$line1"|grep -qE "perl";then
        ext=".pl"
    else
        echo "# "$f" no extension for #! line"
        continue # continue的地方不对
    fi

    newfile="$f$ext"
    if [ -e "$newfile" ];then
        echo "# "$newfile" already exists"     
    else
        echo "mv "$f" "$newfile" "        
    fi

done