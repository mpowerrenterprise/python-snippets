
'''
try:

	prit("Hello")

except Exception as e:
	print("Something went wrong!")






try:

	prit("Hello")

except Exception as e:
	if(str(e) == "name 'prit' is not defined"):
		print("Please check the keyword")


'''



try:

	print("Hello")

except Exception as e:
	if(str(e) == "name 'prit' is not defined"):
		print("Please check the keyword")
finally:
	print("It always works")