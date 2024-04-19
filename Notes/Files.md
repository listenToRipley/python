# Files

## Built in Modules

### os

Package that contains various modules, including path. This is a function approach.

[Examples](../Examples/Files/os.py)

### pathlib

Object-oriented approach to working with files.

[Examples](../Examples/Files/pathlib.py)

## Reading and Writing

Files must be opened and closed when readings.

If you use the `with` keyword, the file will be closed after you read it.

### Write

In the `with open('file_name.type')` you must provide a second argument. The second argument is known as the "mode". The default mode is read, so if the second argument is left out, it is assumed you want to read.

To write to a new file, the mode will be 'w'.

To add to an existing file, use 'a' as your mode. If you don't, use 'a' and still use 'w', it will overwrite the existing concent.

'a' stands for append.

Best practice is the create the path to the file you want to write to if it does not exist in your current directory.

The mode itself won't provide content to be created, it just shows what you will be doing in the file. You will provide the path, file name and the the method associated with the mode to use it.

[Example](../Examples/Files/read_write.py)
