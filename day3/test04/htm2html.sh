#!/bin/dash
##卡了有一会儿，直接用-e判断是否已经存在即可 ,对应题目是如下：
#Your script should stop with EXACTLY the error message shown below 
#and exit status 1 if the .html file already exists.
for f in *.htm;do
    # echo "$f"
    original=$(echo "$f" | sed "s/\.htm//")
    # echo "$original"
    newfile="$original".html
    if [ -e "$newfile" ]; then
        echo "$newfile exists" 1>&2
        exit 1 ## 这里为什么exit1？
    else
        mv "$f" "$newfile"
    fi
   
done
exit 0