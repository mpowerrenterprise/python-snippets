income = [10,30,75]

def double_money(dollers):
	return dollers * 2

new_income = list(map(double_money,income))
print(new_income)

#The map function will call the double_money function 3 times.
#we can do it with for loop, but this one is pertty easy.
#Bellow is the for loop version


#for x in income:
 #	var = double_money(x)
 #	print(var)

