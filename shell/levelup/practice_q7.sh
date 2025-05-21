#!/bin/dash
# 合并了所有的case相似案例，把if elif fi改为了所有的case进行continue
for file_name in "$@"; do
    # 1. 判断是否已有扩展名
    if echo "$file_name" | grep -Eq '\.[A-Za-z]+$'; then
        echo "# $file_name already has an extension"
        continue
    fi

    # 2. 读取第一行
    read -r line < "$file_name"

    # 3. 判断是否有 shebang（#!）
    if ! echo "$line" | grep -Eq "^#!"; then
        echo "# $file_name does not have a #! line"
        continue
    fi

    # 4. 用 case 匹配语言类型
    case "$line" in
        *python*) extension="py"
            ;;
        *sh*) extension="sh"
            ;;
        *perl*) extension="pl"
            ;;
        *)
            echo "# $file_name no extension for #! line"
            continue
            ;;
    esac

    # 5. 构造新文件名
    new_name="$file_name.$extension"

    # 6. 判断目标文件是否已存在
    if [ -f "$new_name" ]; then
        echo "# $new_name already exists"
    else
        echo "mv $file_name $new_name"
    fi
done