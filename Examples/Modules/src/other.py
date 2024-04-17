import Examples.Modules.src.utils as utils

print(utils.hello(utils.my_name))

def sum_fn(a,b):
    return a+b

print("MODULE : OTHER")

print("OTHER ",__name__)
print(type(__name__))