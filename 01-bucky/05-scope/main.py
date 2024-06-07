#global variable can be accessed anywhere in the program in python.
#local variable can be only accessed whithin the function where it has been declared.

a=10 #global variable.

def fun1():

	print(a)

def fun2():
	b=5 # This variable cannot be used out of this function.
	print(b)


fun1();
fun2();