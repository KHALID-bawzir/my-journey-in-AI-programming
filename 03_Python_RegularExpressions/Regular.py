import re
print('phone number:-----')
text1 = '''Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way'''


pattern1 = re.finditer(r'(\d{3})\.(\d{3})\.(\d{4})', text1)

for p in pattern1:
    print(p.group())



print('gmail:----------')

text2 = '''
khalid123@example.com
wnfo.team@mail.net
user_name2025@domain.org
shop.support@store.co
HeLlo.world@test.io
khalid@@gmail.com
user ! name@mail.com
mohammed@.gmail.com
tur-ki@gmail-
ali.space@mail.com
'''

pattern2 = re.compile(r'^[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,6}$')
for line in text2.splitlines():
    line = line.strip()
    if re.match(pattern2, line):
        print(line)

print('number card:--------')

TEXT3 = '''
1111 2222 3333 4444
121371131 1331 6631
1333 33113313 4424
@212.3131 1313 1444-
1311w31131331331-
1333 1331 313133
232 233 2323 23 323-
812 9219 22 92 1299 2. 12 9282
'''

pattern3 = re.compile(r'^(\d{4})\s(\d{4})\s(\d{4})\s(\d{4})$')
for line in TEXT3.splitlines():
    line = line.strip()
    if re.match(pattern3, line):
        print(line)
