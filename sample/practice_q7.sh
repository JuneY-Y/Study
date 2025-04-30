#!/bin/dash

for file in "$@"
do
    # 1. 检查是否已有扩展名
    case "$file" in
        *.*)
            echo "# $file already has an extension"
            continue
            ;;
    esac

    # 2. 检查文件是否存在且是否有 #! 行
    if ! head -n 1 "$file" | grep -q '^#!'; then
        echo "# $file does not have a #! line"
        continue
    fi

    # 3. 获取 shebang 行
    first_line=$(head -n 1 "$file")

    # 4. 判断 shebang 中包含哪些语言
    case "$first_line" in
        *python*) ext=".py" ;;
        *perl*) ext=".pl" ;;
        *sh*) ext=".sh" ;;
        *) echo "# $file no extension for #! line"
           continue ;;
    esac

    new_name="$file$ext"

    # 5. 检查目标文件是否已存在
    if [ -e "$new_name" ]; then
        echo "# $new_name already exists"
        continue
    fi

    # 6. 打印 mv 重命名命令
    echo "mv $file $new_name"
done