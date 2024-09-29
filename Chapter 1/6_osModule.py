import os

# Specify the directory path
directory_path = "/Python/Chapter 1"

# Get the list of files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
