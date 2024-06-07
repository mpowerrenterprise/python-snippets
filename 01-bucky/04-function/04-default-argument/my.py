def genter_user(sex="Unkonwn"): #default argument value value.
	if sex is "M":
	
		sex="Male"

	elif sex is "F":
		sex="Female"

	print(sex)


genter_user("M") # male
genter_user("F") #female
genter_user()  #unkonwn


#if the user does not provide the sex. by deafult it would be assigned Unknown
