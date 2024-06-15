database = ["David", "John", "Mike", "Tim"]

username = input("Enter your username? ")

for x in database:
	if x == username:
		print("Your name has been found in the database")
		break
	else:
		print("Sorry, Your name did not find in the database")


