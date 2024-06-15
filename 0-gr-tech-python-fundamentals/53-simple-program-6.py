phones = {"guna":"23456432","rakulan":"3435643","mike":"324532","tim":"3456434","flo":"324565323","david":"4543245"}


while True:
	user_data = input("Enter the name: ")
	phone_number = phones[user_data]

	print(f"{user_data} : {phone_number}")