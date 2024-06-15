
'''
def print_name(fname, lname, age, job):
	print(f"Hi, My name is {fname} {lname}. I am {age} years old. I am working as a {job}")

print_name(lname= "Rakulan", age="24", job="Software Developer", fname = "Guna")

'''


def print_name(**data):
	print(f"Hi, My name is {data['fname']} {data['lname']}. I am {data['age']} years old. I am working as a {data['job']}")


print_name(fname = "Guna", lname ="Rakulan", age="24", job="Programmer")