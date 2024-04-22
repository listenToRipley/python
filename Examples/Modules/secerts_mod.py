import secrets
import string

#string options
# all_chars = string.ascii_letters + string.digits + string.punctuation

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(all_chars)

# create passwords

# print(secrets.choice(all_chars)) # this will only provide a single elements.

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(list(secrets.choice(all_chars) for i in range(length)))
    return password

print(generate_password(3))
print(generate_password(9))
print(generate_password(15))