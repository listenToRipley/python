import secrets
import string

#string options
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)

all_chars = string.ascii_letters + string.digits + string.punctuation
print(all_chars)
# create passwords

print(secrets.choice(all_chars))