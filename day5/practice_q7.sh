#!/bin/dash

#!/bin/dash

# 题目目的：
# 🌟判断 + 模式匹配 + 控制结构 + I/O判断
# - 给没有扩展名的脚本文件自动添加扩展名（.py / .pl / .sh）
# 考查能力：
# - shebang 解析、条件控制、case语句、文件操作判断

for file in "$@" ##这个是便利所有
do
    # 1. 检查是否已有扩展名
    # case "$file" in
    #     *.*)
    #         echo "# $file already has an extension"
    #         continue
    #         ;;
    # esac
    if echo "$file"|grep -Eq "\.[A-Za-z]+"; then
        echo "# $file already has an extension"
        continue
    fi

 
    # 2. 检查文件是否存在且是否有 #! 行
    if ! head -n 1 "$file" | grep -q '^#!'; then
        echo "# $file does not have a #! line"
        continue
    fi

    # 3. 获取 shebang 行
    first_line=$(head -n 1 "$file")

    # 4. 判断 shebang 中包含哪些语言
    if echo "$first_line"|grep -q "python";then
        ext=".py"
    elif echo "$first_line"|grep -q "perl";then
        ext=".pl"
    elif echo "$first_line"|grep -q "sh";then
        ext=".sh"
    else
        echo "# $file no extension for #! line"
        continue
    fi
    # case "$first_line" in
    #     *python*) ext=".py" ;;
    #     *perl*) ext=".pl" ;;
    #     *sh*) ext=".sh" ;;
    #     *) echo "# $file no extension for #! line"
    #        continue ;;
    # esac

    new_name="$file$ext" 

    # 5. 检查目标文件是否已存在
    if [ -e "$new_name" ]; then  ##-e是用来检查文件是否存在的
        echo "# $new_name already exists"
        continue
    fi

    # 6. 打印 mv 重命名命令
    echo "mv $file $new_name"
done
# echo "$file"