#!/bin/dash
# 本脚本比较两个目录中同名文件的内容，
# 如果目录1中的文件在目录2中存在且内容相同，则输出该文件名（经过排序）。

# 从命令行参数中获取两个目录
dir1="$1"
dir2="$2"

# 遍历目录1中的所有文件
for file in "$dir1"/*; do
    # 取得文件的基本名称（不包含路径）
    filename=$(basename "$file")
    
    # 判断目录2中是否存在同名文件
    if [ -f "$dir2/$filename" ]; then
        # 使用 cmp -s 比较两个文件的内容
        # 如果内容相同，则 cmp 返回 0
        if cmp -s "$file" "$dir2/$filename"; then
            echo "$filename"
        fi
    fi
done | sort




# #!/bin/dash

# dir1="$1"
# dir2="$2"


# for file in "$dir1"/*; do
#     file_name=$(basename "$file")
#     if [ -f "$dir2/$file_name" ] && cmp -s "$file" "$dir2/$file_name"; then
#         echo "$file_name"
#     fi
# done | sort