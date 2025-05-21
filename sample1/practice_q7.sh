#!/bin/dash
filename=$1 ##这里也不用进行变量的赋值，为什么呢？
for filename in "$@";do

    #./practice_q7.sh: 4: cannot open script.rs: No such file
    if [ ! -f "$filename" ]; then
        echo "# $filename not found"
        continue
    fi 
    read -r line < "$filename"  #这里还是没有特别想出来
    case "$line" in
        *perl*) extension="pl";;
        *python*) extension="py";;
        *sh*) extension="sh";;
        *) extension="";;
    esac


    newfilename=$("$filename.$extension")

    if echo "$filename" |grep -E "\.[A-Za-z]+";then
        echo "# filename already has an extension"
    elif [ "$(head -1 "$filename")" != "#!" ]; then   ## 这里是个什么写法呢？
        echo "# filename does not have a #! line"
    elif [ "$(head -1 "$filename")" != "python|sh|perl" ];then
        echo "# filename no extension for #! line"
    elif echo "$newfilename" |grep -E "\.[A-Za-z]+";then
        echo "# filename.<ext> already exists"
    else
        echo "mv filename filename.<ext>"
    fi

done