#/bin/dash

file=$1

# for lines in "$file";do
#     line=(r"$line|sort -n")
# done

numbers=$(cat "$file"| sort -n)
start=$(echo "$numbers"|head -n1)
end=$(echo "$numbers"|tail -n1)
# echo "$numbers" "$start" "$end"
count=$start

while ( $count -le $end );do
    count=$((count+1))
done