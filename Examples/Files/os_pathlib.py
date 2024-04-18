from os import path
from pathlib import Path

# os
print(path.abspath('.'))
# ~/Documents/GitHub/python/

print(type(path))

# pathlib
print(Path('.').absolute())
# ~/Documents/GitHub/python/

print(type(Path))
