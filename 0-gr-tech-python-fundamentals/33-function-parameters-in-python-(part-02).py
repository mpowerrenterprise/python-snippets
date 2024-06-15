def fullNameFunction(fname, lname, age):
	print(f"My full name is {fname} {lname}, and I am {age} years old")


fullNameFunction("Gunarakulan", "Gunaretnam", "23")

fullNameFunction("David", "Frank", "32")



def add_function(num1, num2):
	print(num1 + num2)


def sub_function(num1, num2):
	print(num1 - num2)

add_function(12, 8)
add_function(120,30)

sub_function(10, 5)
sub_function(100, 5)



def add_function(num1, num2, operator):

	if(operator == "+"):
		print(num1 + num2)

	elif(operator == "-"):
		print(num1 - num2)

	elif(operator == "*"):
		print(num1 * num2)

	elif(operator == "/"):
		print(num1 / num2)



number1 = int(input("Enter number one "))
number2 = int(input("Enter number two "))

operator = input("What do you want to do (-, +, *, /)?")

add_function(number1, number2, operator)