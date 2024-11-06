from path_lib import Path

# read

# with open('test.txt') as test_file: #test_file is an object.
#     print(test_file.read())#show concents of the file
#     # or
#     print(test_file.readlines()) # lists of strings seperated by \n

# write
# with open('new.txt', 'w') as new_file:
#     new_file.write("First line of the new file \n")

# with open('new.txt') as new_file:
#     print(new_file.read()) #output new file

# with open('new.txt', 'a') as new_file:
#     new_file.write("second line in the new file\n")

# with open('new.txt') as new_file:
#     print(new_file.read()) #output new file

file_path = Path('Examples/Files/my_file.txt')
# This is not ideal formatting
# file = open(file_path, 'w')
# print(file)
# print(type(file))

# file.write("First line\n")
# file.write("Second line \n")

# #now close
# file.close()

#now you can read
# file = open(file_path)
# print(file.read())

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line \n")

with open(file_path) as file:
    #read each lines of code
    # for line in file.readlines():
    #     print(line.strip())
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())

with open(file_path, 'a') as file:
    file.write("Third line\n")

with open(file_path) as file:
    print(file.read())


if file_path.exists():
    file_path.unlink()