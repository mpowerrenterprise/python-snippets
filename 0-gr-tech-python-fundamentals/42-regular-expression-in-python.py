import re

text = "Hello, My name is Gunarakulan, My phone number is 1234567890. I like %$^&*(&^%$#&^"

result = re.findall("[0-9]", text)

print(result)


#[a-z]
#[A-Z]
#[a-zA-Z]
