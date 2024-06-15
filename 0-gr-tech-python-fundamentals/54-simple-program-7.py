import os 
import random  


user_input = int(input("How many folders do you want to create? "))


for x in range(user_input):
	folder_name = random.randrange(1000, 10000)
	os.mkdir(str(folder_name))


