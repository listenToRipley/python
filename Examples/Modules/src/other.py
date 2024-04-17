import sys
sys.path.insert(0,"../")

import utils as utils
from main import initialize 

print(utils.hello(utils.my_name))

def sum_fn(a,b):
    return a+b

print("MODULE : OTHER")

print("OTHER ",__name__)
print(type(__name__))

initialize()