#!/bin/bash

# Get the directory of the script
script_dir="$(dirname "$0")"

# Define the target directory
target_dir="~/Library/Keyboard Layouts"

# Ensure the target directory exists
mkdir -p "$target_dir"

# Copy the .bundle file to the target directory
cp "$script_dir/सरळसंस्कृतं.bundle" "$target_dir/"

echo "Keyboard layout installed successfully."