import sys

print(sys.argv)

if len(sys.argv) < 3:
  raise IOError("You must provide username and password")

# username = sys.argv[1]
# password = sys.argv[2]

_, username, password = sys.argv

print(f"Username: {username} \nPassword: {password}")

print(sys.version_info)
print(sys.version)
print(sys.base_prefix)