#!/bin/dash

filename=$1
courses=$(cut -d'|' -f1 "$filename"|sort|uniq)
# echo "$courses"
for course in $courses; do
    male_count=$(grep "^$course|" "$filename"|grep -c "|M$") ##grep -c仅仅显示匹配的行数1
    filename_count=$(grep "^$course|" "$filename"|greo -c )
done
# #!/bin/dash
# filename=$1
# echo $filename
# count_man=$(grep -E "\|M$" "$filename")
# echo "$count_man"
# count_woman=$(grep -E "\|F$" "$filename")
# echo "$count_woman"
# # while read -r "$filename"; do
# for line1 in "$count_man"; do
#     for line2 in "$count_woman"; do
#         man=$(grep -E "^[A-Za-z]{4}[0-9]{4}" "$line1"|wc -l)
#         woman=$(grep -E "^[A-Za-z]{4}[0-9]{4}" "$line2"|wc -l)
#         if [ "$man" -eq "$woman" ];then
#             echo "result:"
#             result=$(grep -oE "^[A-Za-z]{4}[0-9]{4}" '$line1'|cut -d '|' -f1)
#             # echo $(grep -Eo "^[A-Za-z]{4}[0-9]{4}" "$line1")
#             echo $result
#         fi
#     done
# done

# # done