import random

data = "qwertyuiop[]asdfghjkl;'zxcvbnm,./`1234567890-=QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?~!@#$%^&*()_+"

length = int(input("Please enter the length of the password that you want to generate? "))

generated_password = "".join(random.sample(data, length))

print(f"The generated password is:- {generated_password}")


