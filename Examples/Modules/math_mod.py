import math

# print(math.e)
# print(math.pi)
# print(math.sqrt(230))
# print(math.factorial(10))
# print(math.log10(100))
# print(math.log2(8))
# print(math.floor(10.7))
# print(round(10.7))

#recursion 
def calc_factorial(num: int):
    if type(num) is not int:
        raise TypeError("Number must be an integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    
    if num == 1:
        return 1
    return num * calc_factorial(num - 1 ) 

print(calc_factorial(10))
