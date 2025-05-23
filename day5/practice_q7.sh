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

    if echo "$first_line"| grep -Eq "perl";then
        ext=".pl"
    elif echo "$first_line"| grep -Eq "sh";then
        ext=".sh"
    elif echo "$first_line"| grep -Eq "python";then
        ext=".py"
        # continue 不需要在这里continue
    else
        echo "# $file no extension for #! line"
        continue
    fi

    new_name="$file$ext" ##🌟这里用引号进行拼接
    if [ -e "$new_name" ]; then ## 逻辑依旧写反了
        echo "# $new_name already exists"
    else
        echo "mv $file $new_name"
    fi

done