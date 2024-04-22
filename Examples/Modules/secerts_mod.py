import secrets
import string

#string options
all_chars_list = string.ascii_letters + string.digits + string.punctuation

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(all_chars)

# create passwords

# print(secrets.choice(all_chars)) # this will only provide a single elements.

#count how many times we go through this function 
counter = 0
def generate_password(length: int):
    global counter 
    counter += 1
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(list(secrets.choice(all_chars) for i in range(length)))
    return password

def generate_special_password(length:int):
    while True:
        password = generate_password(length)
        #check if we pass each of the requirements
        has_lower = (any(char.islower() for char in password))
        has_upper = (any(char.isupper() for char in password))
        has_digit = (any(char.isdigit() for char in password))
        has_pun = (any(char in string.punctuation for char in password))
        if has_lower and has_upper and has_digit and has_pun:
            break
    return password


# print(generate_password(3))
# print(generate_password(9))
# print(generate_password(15))

print(f"Special password: {generate_special_password(6)}")
print(f"Go through the generation process : {counter} times")
# generated csrf tokens (session token)

print(secrets.token_hex(8))
print(secrets.token_hex(16))
print(secrets.token_hex(24))

# token urls - one time use. safe for one time use url param

print(secrets.token_urlsafe())
print(secrets.token_urlsafe(16))

# otp passwords
def generate_otp_password(length):
    digits = string.digits
    password ="".join(secrets.choice(digits) for _ in range(length))
    return password

print(generate_otp_password(10))
print(generate_otp_password(6))
print(generate_otp_password(4))