#!/bin/dash

filename="$1"

n=$(sort -n "$filename"| head -n 1)
m=$(sort -n "$filename"| tail -n 1)

start="$n"

echo $start

# #!/bin/dash

# file="$1" ##

# n=$(sort -n "$file" | head -n 1)
# m=$(sort -n "$file" | tail -n 1) ## file这里让他不是硬编码 

# expected=$(mktemp)
# actual=$(mktemp)

# seq "$n" "$m" > "$expected"
# sort -n "$file" > "$actual"

# diff "$actual" "$expected" | grep '^>' |cut -d " " -f2 

# rm -f "$expected" "$actual"  ##
