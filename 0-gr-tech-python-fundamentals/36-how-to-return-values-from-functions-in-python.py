'''

def print_name(data):
	for x in data:
		print(f"My name is {x}")


names1 = ["Guna", "Rakulan", "Kim", "Tim"]
names2 = ["David", "Frank", "Job", "Bill"]



print_name(names1)

print_name(names2)




def print_name(data):
	for k in data:
		print(f"{k} : {data[k]}")



dic1 = {"name":"guna", "age":"24", "job":"Developer"}

print_name(dic1)


def print_name():
	return "Hello"


name = print_name()

print(name)


'''


def addition(*numbers):

	total = 0

	for x in numbers:
		total = total + x

	return total

print(addition(12,23,43,45,5))

