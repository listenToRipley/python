from array import array

int_array = array('i', [10,4,3,7,9,15]) # since you specified the type, other types will not be allowed.
# print(int_array)
# print(type(int_array))
# print(dir(int_array))
# print(int_array[2])

# int_array.append(20)
# int_array.append(True) # example of a converted value to the type of the array.
# print(int_array)
# int_array.pop()
# print(int_array)

#add array to a file - usually saved as binary files
with open('my_array.bin', 'wb') as file:
  int_array.tofile(file)