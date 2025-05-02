#!/bin/dash
# ==============================================================================
# name: compare_dirs.sh
# aim: Compare files in two directories by name and content (ignoring case/space)
#
# Usage: ./compare_dirs.sh dir1 dir2
# ==============================================================================

dir1="$1"
dir2="$2"

# Check if both arguments are valid directories
if [ ! -d "$dir1" ] || [ ! -d "$dir2" ]; then
    echo "Usage: $0 <dir1> <dir2>"
    echo "Both arguments must be valid directories."
    exit 1
fi

# Loop through all files in dir1
for file1 in "$dir1"/*
do
    file_name=$(basename "$file1")  # Extract file name
    file2="$dir2/$file_name"        # Corresponding file in dir2

    if [ -e "$file2" ]; then
        if diff -i -w "$file1" "$file2" >/dev/null; then
            echo "$file_name"  # Output matching files
        fi
    fi
done