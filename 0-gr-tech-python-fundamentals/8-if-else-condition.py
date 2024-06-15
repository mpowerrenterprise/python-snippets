database_username = "gunarakulan"
database_password = "guna12345"


user_entered_username = input("Please enter your username? ")
user_entered_password = input("Please enter your password? ")

                         
if database_username == user_entered_username and database_password == user_entered_password:
	print("You are logged in")

else:
	print("Username or password is wrong")



