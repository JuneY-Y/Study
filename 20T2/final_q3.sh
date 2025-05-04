

cut -d, -f1 enrollments.txt | sort | uniq -c | while read count student_id; do
    if [ "$count" -eq "2" ]; then
        echo $student_id
    fi
done