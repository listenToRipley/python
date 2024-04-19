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

file_path = 'Examples/Files/my_file.txt'
file = open(file_path, 'w')
print(file)
print(type(file))

file.write("First line\n")
file.write("Second line \n")

#now close
file.close()

#now you can read
file = open(file_path)
file.read()