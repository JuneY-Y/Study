#!/bin/dash
# ==============================================================================
# name: final_q6.sh
# aim: Print ln -s commands for files with identical contents 

# 经验： 这次总是搞混 for file in "$@" 这里不需要加上冒号的
# Written by: z5452842 JiamingYang
# For COMP2041/9044 Final Q6
# ==============================================================================

found=false
seen_files=""

# input时间
for file in "$@"
do
    for seen in $seen_files
    do
        if cmp -s "$file" "$seen"; then
            echo "ln -s $seen $file"
            found=true
            break
        fi
    done

    # 将当前文件添加到“已处理列表”
    seen_files="$seen_files $file"
done

# 如果没找到任何可替换的文件，打印提示
if [ "$found" = false ]; then
    echo "No files can be replaced with symbolic links"
fi


