person1 = {"name":"david", "age":66, "job":"Web Developer", "From":"USA"}



# Method 1

for x in person1:
	print(person1[x])

# Method 2

for x in person1.keys():
	print(person1[x])

# Method 3

for x in person1.values():
	print(x)

# Method 4

for k, v in person1.items():
	print(f'{k}  {v}')