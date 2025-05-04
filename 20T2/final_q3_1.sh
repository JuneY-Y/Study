cut -d '|' -f2 enrollments.txt | sort | uniq -c | while read count student_id ; do
    if [ "$count" -eq 1 ];then # 一个段落，会有 ";"
        echo "$student_id"
    fi
done 
