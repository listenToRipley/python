# import utils
# import utils as u
# from utils import hello, my_name as name
from src import utils as my_utils
# from src.other import sum_fn
import math

# print(utils)
# print(type(utils))
# print(dir(utils))

# print(utils.my_name)
# print(u.hello(u.my_name))
# print(hello(name))

# print(sum_fn(10,2))

print(my_utils.hello(my_utils.my_name))

print(type(math))

def initialize():
    # Code to initialize application and perform setup.
    print("initializing...")

def main():
    # Code for main app functionality.
    print("Running main block functionality")

print("MAIN : ",__name__)
print(type(__name__))

if  __name__ == '__main__':
    # Only if run directly
    initialize()
    main()