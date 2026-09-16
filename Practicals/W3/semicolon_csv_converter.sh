#!/bin/bash
# semicolon_csv_converter.sh
# Converts a semicolon-delimited file to a comma-delimited file.
# Usage: bash semicolon_csv_converter.sh file_to_convert.csv

# Check that an argument was provided
if [ -z "$1" ]; then
    echo "Usage: bash semicolon_csv_converter.sh <file_to_convert>"
    exit 1
fi

input_file="$1"

# Check that the file exists
if [ ! -f "$input_file" ]; then
    echo "Error: file '$input_file' not found."
    exit 1
fi

# Build the output filename by inserting "_converted" before the extension
filename="${input_file%.*}"
extension="${input_file##*.}"
output_file="${filename}_converted.${extension}"

# Replace all semicolons with commas, write to the new file
sed 's/;/,/g' "$input_file" > "$output_file"

echo "Converted file saved as: $output_file"
