#!/bin/dash

for htm_file in *.htm; do
    if [ "$htm_file" = "*.htm" ]; then
        exit 0
    fi
    html_filename="${htm_file%.*}.html"
    if [ -f "$html_filename" ]; then
        echo "$html_filename exists"
        exit 1
    fi
    mv "$htm_file" "$html_filename"
done


# #!/bin/dash

# ## 修改htm为html
# for htm_file in *.htm;do
#     if [ "$htm_file" = "*.htm" ]; then
#         exit 0
#     fi
#     html_filename="${htm_file%.*}.html"
#     if [ -f "$html_filename" ]; then
#         echo "$html_filename exists"
#         exit 1
#     fi
#     mv "$htm_file" "$html_filename"
# done
