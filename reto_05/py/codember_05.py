import re

with open(r'..\file.txt', 'r') as f:
    values = f.read().splitlines()

for value in values:
    id, username, email, age, location = value.split(',')

    if (id and not id.isalnum()) or (username and not username.isalnum()) or (email and not re.findall(r'[A-z0-9]+@[A-z0-9]+\.com', email) or not email) or (age and not age.isnumeric()):
        print(username[0], end='')
    else:
        continue
