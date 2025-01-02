#!/usr/bin/env bash

# curl command to download dataset from kaggle
# curl -L -o $folder_path/$zip_file $kaggle_url

# Ensure the script is executable
chmod +x $0

# Check if the required arguments are provided
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage rules: Please also add the <output_filename> and <kaggle_url> as command-line arguments"
  exit 1
fi


# Define the folder path 
folder_path="/Users/imran-m/Python-projects/10-data_manipulation"


# Download the dataset from Kaggle
curl -L -o "$folder_path/$1" "$2"