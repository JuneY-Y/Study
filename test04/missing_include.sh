#!/bin/dash

# Loop over all filenames passed as command-line arguments
for file in "$@" ; do

    # Find all lines in the file that include local headers (e.g. #include "file.h")
    grep -e "#include \".*\.h\"" "$file" | \

    # Read each matching line one by one
    while read -r line; do

        # Extract the header filename between the double quotes using cut
        head_file=$(echo "$line" | cut -d"\"" -f2)

        # If the header file does NOT exist in the current directory
        if [ ! -f "$head_file" ]; then

            # Print a warning message that the included header file is missing
            echo "$head_file included into $file does not exist"
        fi

    done

done