from os import path
from pathlib import Path

print(Path('.').absolute())
# ~/Documents/GitHub/python/

print(type(Path))

file_path = Path('test.txt')

print([m for m in dir(file_path)
       if not m.startswith('_')])

# find path on the *current* directory
print(Path.cwd())

# create new path
print(Path('usr').joinpath('local').joinpath('bin'))
# or
print(Path('usr') / 'local' / 'bin')

# Checking the *current directory* presence of the directory or file
print(Path('main.py').exists())
print(Path('home/nken/Documents').exists())
print(Path('other.py').exists())
# these are absolute paths

print(Path('os_pathlib.py').is_file())
print(Path('../Files').is_file())
print(Path('../Files').is_dir())

# list of files and folders
for f in Path('.').iterdir():
    print(f)