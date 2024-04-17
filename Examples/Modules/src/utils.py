def hello(name):
    return f"Hello {name}"

my_name = "Natalie"

print("MODULE: UTILS")

print("UTILS",__name__)
print(type(__name__))

print("UTILS", __name__ == '__main__')
print("UTILS", __name__ == 'src.utils')