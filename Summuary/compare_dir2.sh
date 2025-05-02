if [ $# -lt 2 ]; then
    echo "Usage: $0 <dir2> <dir2>"
    echo "must be two directory"
    exit 1
fi

if [ -z "$dir1" ]; then
    echo ""