#!/bin/dash

newfilename=$("$filename.$extension")
for filename in "$@";do
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