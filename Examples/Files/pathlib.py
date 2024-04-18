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

# Check if the directory exists
# if not directory_path.exists():
#     #create directory
#     directory_path.mkdir()
#     print(f"Directory was created : {directory_path}")
# else:
#     print(f"Directory already exists : {directory_path}")

# Create path to the file

# Getting parent directory