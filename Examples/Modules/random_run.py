import random

#float
print(random.random())
print(random.uniform(10.5,11.6))

#int 
print(random.randint(100,1000))

# shuffle 
# tuples are not allowed since they are immutable.
# sets are also not allowed since they are unordered
my_list = [1,2,3,4,5,6,7]
print(f"original list : {my_list}")
random.shuffle(my_list)
print(f"shuffled list : {my_list}")
random.shuffle(my_list)
print(f"shuffled again list : {my_list}")
random.shuffle(my_list)

# choice
# dictionary are not allowed
print(f"Choice: {random.choice("Natalie")}")
print(f"Choice: {random.choice((1,2,3,4,5))}")
print(f"Choice: {random.choice(['a', 'b', 'c'])}")

#choices - doesn't promise unique elements.
print(f"Choices : {random.choices([1,2,3,4,5,6,7,8], k=3)}")
print(f"Choices : {random.choices('whatdoyouwant', k=7)}")
print(f"Not best practice to make a password : {''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz', k=12))}")

# sample - promises unique elements
print(f"Sample: {random.sample([1,2,3,4,5,6,7,8], k=3)}") # k cannot exceed the length of the element provided.
print(f"Sample password, not greate either : {''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz', k=12))}")
print(random.sample([1,1,1,1,1], k=3)) # this won't produce an error since each values is treated as a unique item.
print(random.sample(range(1_000_000),k=10))