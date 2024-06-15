objects1 = ("bmw", "david", "Mike", "tim")
objects2 = ("table", "phone", "laptop")

totalObjects = objects1 + objects2

convertedToList = list(totalObjects)

convertedToList.append("Last Element")


print(convertedToList)

print(type(convertedToList))


for x in totalObjects:
	print(f"Object name is {x}")

