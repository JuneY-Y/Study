#!/bin/dash

for file_name in "$@"; do
    ## 可以重新再写个if 进行判断是否有已经有的扩展名，直接输出即可
    if echo "$file_name" | grep -Eq '\.[A-Za-z]+$'; then
        echo "# $file_name already has an extension"
        continue ##加continue可以继续下一个if 逻辑
    fi
    # case "$(head -1 "$pathname")" in
    #     *perll*
    # esac
    # cat "$file_name" | head -n 1 | while read -r line; do
    read -r line < "$file_name" ## 读取$file_name的第一行

    if ! echo "$line" | grep -Eq "^#!"; then
        echo "# $file_name does not have a #! line"
    elif ! echo "$line" | grep -Eq "^#!.*(python|sh|perl)"; then
        echo "# $file_name no extension for #! line"
    elif echo "$line"|grep -Eq "^#!.*python"; then
        if [ -f "$file_name.py" ]; then
            echo "# $file_name.py already exists"
        else
            echo "mv $file_name $file_name.py"
        fi
    elif echo "$line"|grep -Eq "^#!.*sh"; then
        if [ -f "$file_name.sh" ]; then
            echo "# $file_name.sh already exists"
        else
            echo "mv $file_name $file_name.sh"
        fi
    elif echo "$line"|grep -Eq "^#!.*perl"; then
        if [ -f "$file_name.pl" ]; then
            echo "# $file_name.pl already exists"
        else
            echo "mv $file_name $file_name.pl"
        fi
    fi
    # done
done