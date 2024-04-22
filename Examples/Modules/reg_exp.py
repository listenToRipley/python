import re

my_string = "My name is Natalie."
# $ is for the end of the string
# ^ is the start of the string
# . any character
# * any number of times
# \ escape character for special characters
result = re.search(r'^M.*Natalie\.$', my_string)
print(result)
# print(type(result))
# print(dir(result))
# print(r'^M.*Natalie$\n') # r string, allow all special characters to be treated as a regular string of characters. 
# # r strings can be used in conjuction with regex to create a pattern.
# print(result.span())
# print(result.start())
# print(result.end())

new_pattern = re.compile(r'N.....e')
print(type(new_pattern))
print(new_pattern.search(my_string))
print(new_pattern.search("we need Naature now."))
print(new_pattern.findall("My name is Natalie. Say hello to Naature!!"))

def validate_email(email:str):
    email_regexp = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email_pattern = re.compile(email_regexp)
    is_valid = bool(email_pattern.match(email))
    return (email, is_valid)

print(validate_email('a.dent@example.com'))
print(validate_email('a.dentexample.com'))
print(validate_email('@a.dentexample.com'))


reg_exp = r'bit'

my_text = "Nuns aren't supposed to develope bad habits in this habits, like putting them on rabbits."

change_text = re.sub(reg_exp, '*', my_text)
print(change_text)

my_unformatted_text = " THIS  is a horribly              unformatted sentence.    Way,         to long."
regexp = r'\s+'
fixed = ' '.join(re.split(regexp, my_unformatted_text))
print(fixed)