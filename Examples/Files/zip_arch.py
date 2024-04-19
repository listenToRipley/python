from zipfile import ZipFile
from pathlib import Path

my_dir = Path('Examples/Files/ZipTest')
if not my_dir.exists():
    my_dir.mkdir()

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