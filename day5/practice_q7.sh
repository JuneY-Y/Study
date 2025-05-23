#!/bin/dash

for file in "$@"; do
    if echo "$file"| grep -Eq "\.[A-Za-z]+"; then
        echo "# $file already has an extension"
        continue
    fi

    if ! head -n 1 "$file"|grep -Eq "^#!"; then ## 注意 ！有还是没有
        echo "# $file does not have a #! line"
        continue
    fi

    ##If the #! line does not contain any of the strings, perl, python or sh,
    #所以需要先获取shebang
    first_line=$(head -n 1 "$file")
    if echo "$first_line"| grep -Eq "perl|sh|perl";then
        echo "# $file does not have a #! line"
        continue
    fi

done