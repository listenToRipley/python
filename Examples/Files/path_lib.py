from pathlib import Path

# print(Path('.').absolute())

# print(type(Path))

# file_path = Path('test.txt')

# print([m for m in dir(file_path)
#        if not m.startswith('_')])

# # find path on the *current* directory
# print(Path.cwd())

# # create new path
# print(Path('usr').joinpath('local').joinpath('bin'))
# # or
# print(Path('usr') / 'local' / 'bin')

# # Checking the *current directory* presence of the directory or file
# print(Path('main.py').exists())
# print(Path('home/nken/Documents').exists())
# print(Path('other.py').exists())
# # these are absolute paths

# print(Path('os_pathlib.py').is_file())
# print(Path('../Files').is_file())
# print(Path('../Files').is_dir())

# # list of files and folders
# for f in Path('.').iterdir():
#     print(f)

# Directory path
directory_path = Path('my_test_directory')

print(type(directory_path))

print(Path.__subclasses__())

# Check if the directory exists
if not directory_path.exists():
    #create directory
    directory_path.mkdir()
    print(f"Directory was created : {directory_path}")
else:
    print(f"Directory already exists : {directory_path}")

# Create path to the file
file_path = directory_path / 'my_file.txt'
other_file_path = directory_path.joinpath('my_file.txt')
print(f"File path is {file_path}")

# Getting parent directory
parent_dir = file_path.parent
print(f" Parent directory {parent_dir}")

#Checking if the file is file path or dir path
is_file = file_path.is_file()
is_dir = directory_path.is_dir()

print(f"{file_path} is a file? {is_file} \n {directory_path} is a directory? {is_dir}")

# Listing files in the directory through iteration

files = [file for file in directory_path.iterdir()] 
# can add .name to file to just get the file name
files_detailed = [file.name for file in directory_path.iterdir() if file.is_file()]
# to just return if there are files, not directories. 

print(f"Files in the directory: {files}")

# Remove directory
if directory_path.exists():
    files = [file for file in directory_path.iterdir()] 
    for file in files:
        file.unlink()        
    directory_path.rmdir()