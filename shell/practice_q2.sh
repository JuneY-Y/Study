#!/bin/dash
filename=$1
echo $filename
count_man=$(grep -E "\|M$" "$filename")
echo "$count_man"
count_woman=$(grep -E "\|F$" "$filename")
echo "$count_woman"
# while read -r "$filename"; do
for line1 in "$count_man"; do
    for line2 in "$count_woman"; do
        man=$(grep -qE "^[A-Za-z]{4}[0-9]{4}" "$line1"|wc -l)
        woman=$(grep -qE "^[A-Za-z]{4}[0-9]{4}" "$line2"|wc -l)
        if [ "$man" -eq "$woman" ];then
            echo $(grep -qE "^[A-Za-z]{4}[0-9]{4}" "$line1")
        fi
    done
done

# done