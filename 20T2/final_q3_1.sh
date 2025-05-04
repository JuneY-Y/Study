cut -d, -f1 enrollments.txt | sort | uniq -c | while read count student_id ; do
    if [ "count" -eq 1 ]; # 一个段落，会有 ";"
    echo "$student_id"
    fi
done 