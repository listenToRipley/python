import json 

my_nums = [10,100,58,20]

my_nums_json = json.dumps(my_nums)

print(type(my_nums_json))
print('list',my_nums_json)

my_nums_tup = (10,100,58,20)

my_nums_json_2 = json.dumps(my_nums_tup)

print(type(my_nums_json_2))
print('tuple',my_nums_json_2)

# Typeerror sets are not json format possible
# my_nums_set = {10,100,58,20}

# my_nums_json_3 = json.dumps(my_nums_set)

# print(type(my_nums_json_3))
# print(my_nums_json_3)

# dictionary
my_post = {
    'title': "post name",
    'content': "post content",
    'likes_qty': 25,
    'author': {
        'username': 'dent.a',
        'email': 'adent@gmail.com'
    },
    'metadata': (5,7,25)
}

my_post_json = json.dumps(my_post)
print(type(my_post_json))
print("POST : ",my_post_json)

dic_back = json.loads(my_post_json)
print(type(dic_back))
print(dic_back) #now tuple is a list.

#dict with function

def sum_fn(a,b):

    return a+b
my_math  = {
    'title': "Math dic",
    'sum': sum_fn
}

# math_json = json.dumps(my_math)

# print(math_json)

