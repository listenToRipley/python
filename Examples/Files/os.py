# from os import path
import os

# print(path.abspath('.'))

# print(type(path))

directory_path = 'my_test_directory'

if not os.path.exists(directory_path):
    # create directory
    os.mkdir(directory_path)
    print(f"Directory was created: {directory_path}")
else:
    print(f"Directory exists: {directory_path}")
# Create path to file
file_path = os.path.join(directory_path, 'my_file.txt')
print(f"File path: {file_path}")

# get parent directory since the relationship is relative
parent_dir = os.path.dirname(file_path)
print(f"Parent directory: {parent_dir}")

# checking if file is the file or dir path.
is_file = os.path.isfile(file_path)
is_dir  = os.path.isdir(directory_path)

print(f"{file_path} is a file? {is_file}")
print(f"{directory_path} is a directory? {is_dir}")

# Listing Files in the the directory
dir_files = os.listdir(directory_path)
for file in dir_files:
    print(file)


# Remove directory
if os.path.exists(directory_path):
    for file in dir_files:
        os.remove(os.path.join(directory_path, file))
    os.rmdir(directory_path) # cannot be removed if the directory has files.
    print(f"Directory {directory_path} was removed")