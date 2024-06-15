while True:

	user_input = input("Enter something: ")

	f = open("data.txt", "at")
	f.write(user_input+"\n")

	if(user_input == "[STOP]"):
		f.close()
		break