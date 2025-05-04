#!/bin/dash

printed=0
processed=""

for file1 in "$@"; do
    # file1 如果被处理过就跳过（避免成为 file2）
    case "$processed" in
        *" $file1 "*) continue ;;
    esac

    for file2 in "$@"; do
        # file1 不和自己比
        [ "$file1" = "$file2" ] && continue

        # file2 处理过就跳过
        case "$processed" in
            *" $file2 "*) continue ;;
        esac

        if cmp -s "$file1" "$file2"; then
            echo "ln -s $file1 $file2"
            printed=1
            processed="$processed $file2 "
        fi
    done

    processed="$processed $file1 "
done

test "$printed" -eq 0 && echo "No files can be replaced by symbolic links"