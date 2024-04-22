from zipfile import ZipFile
from pathlib import Path

my_dir = Path('Examples/Files/ZipTest') # directory path
if not my_dir.exists(): #create directory if it doesn't exist
    my_dir.mkdir()

# remove zip file if it exists
zip_archive = Path('Examples/Files/zip-test.zip')
if zip_archive.exists():
    zip_archive.unlink()

file_one = 'Examples/Files/ZipTest/first.txt'
file_two = 'Examples/Files/ZipTest/second.txt'

with open(file_one, 'w') as file:
    file.write("First line in this file\n")


with open(file_two, 'w') as file:
    file.write("First line in this file\n")  

# Create zip
with ZipFile('Examples/Files/zip-test.zip', mode='w') as zip_file:
    for file in my_dir.iterdir():
        print(file)
        zip_file.write(file)

# Open zip
with ZipFile(zip_archive) as zip_file:
    print(zip_file)
    print(type(zip_file))
    print(zip_file.compression)
    print(zip_file.infolist())
    # unpack
    zip_file.extractall('unzip_files')
    # specific  files to extract
    zip_file.extract(file_two, 'Examples/Files')