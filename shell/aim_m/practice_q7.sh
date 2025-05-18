#!/bin/dash

for file_name in "$@"; do
    # 读取第一行的 shebang 行
    cat "$file_name" | head -n 1 | while read -r line; do

        # 情况 1：不是以 #! 开头，说明不是脚本文件
        if ! echo "$line" | grep -Eq "^#!"; then
            echo "$file_name does not have a #! line"

        # 情况 2：虽然以 #! 开头，但不包含 python/sh/perl
        elif ! echo "$line" | grep -Eq "^#!.*(python|sh|perl)"; then
            echo "$file_name no extension for shebang line"

        # 情况 3：是 Python 脚本
        elif echo "$line" | grep -Eq "^#!.*python"; then
            if [ -f "$file_name.py" ]; then
                echo "$file_name.py already exists"
            else
                echo "mv $file_name $file_name.py"
            fi

        # 情况 4：是 Shell 脚本
        elif echo "$line" | grep -Eq "^#!.*sh"; then
            if [ -f "$file_name.sh" ]; then
                echo "$file_name.sh already exists"
            else
                echo "mv $file_name $file_name.sh"
            fi

        # 情况 5：是 Perl 脚本
        elif echo "$line" | grep -Eq "^#!.*perl"; then
            if [ -f "$file_name.pl" ]; then
                echo "$file_name.pl already exists"
            else
                echo "mv $file_name $file_name.pl"
            fi
        fi

    done
done
# #!/bin/dash

# for file_name in "$@"; do
#     # case "$(head -1 "$pathname")" in
#     #     *perll*
#     # esac
#     cat "$file_name" | head -n 1 | while read -r line; do

#     if ! echo "$line" | grep -Eq "^#!"; then
#         echo "# $file_name does not have a #! line"
#     elif ! echo "$line" | grep -Eq "^#!.*(python|sh|perl)"; then
#         echo "# $file_name no extension for #! line"
#     elif echo "$line"|grep -Eq "^#!.*python"; then
#         if [ -f "$file_name.py" ]; then
#             echo "# $file_name.py already exists"
#         else
#             echo "mv $file_name $file_name.py"
#         fi
#     elif echo "$line"|grep -Eq "^#!.*sh"; then
#         if [ -f "$file_name.sh" ]; then
#             echo "# $file_name.sh already exists"
#         else
#             echo "mv $file_name $file_name.sh"
#         fi
#     elif echo "$line"|grep -Eq "^#!.*perl"; then
#         if [ -f "$file_name.pl" ]; then
#             echo "# $file_name.pl already exists"
#         else
#             echo "mv $file_name $file_name.pl"
#         fi
#     fi
#     done
# done