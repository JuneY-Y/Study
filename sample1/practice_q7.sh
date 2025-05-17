#!/bin/dash
## 直接with open file,但是shell里面应该是 read -r
# 这里面应该是while read -r; do done?
#读取第一行，咋读啊
#如果没有if fi那么进行添加（题意是不需要添加的） extension就是开头那个破东西
#识别的话 regex=$(grep -xE "^[#!]/.*")
#添加成功以后推出

for pathname in "$@"; do  ##想不明白，为什么要读取pathname
    case "$(head -1 "$pathname")" in
        *perl*) extension="pl";;
        *python*) extension="py";;
        *sh*) extension="sh";;
        *) extension="";;
    esac

    new_pathname="$pathname.$extension"

    if echo "$pathname" | grep -Eq '\.[^/]+$'; then
        echo "# $pathname already has an extension"
    elif [ "$(head -c 2 "$pathname")" != '#!' ];then
        echo "# $pathname does not have a #! line"
    elif [ -z "$extension" ];then
        echo "# $pathname no extension for #! line"
    elif [ -e "$new_pathname" ]; then
        echo "# $new_pathname already exists"
    else
        echo "mv $ppathname $new_pathname"
    fi

done