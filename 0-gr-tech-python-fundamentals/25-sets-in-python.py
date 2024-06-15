#list
#tuple
#set

#random
#loop
#checking
#add
#update
#len
#remove
#discard
#pop()
#clear



objects = {"daivd", "table", "laptop", "phone", "Mike"} # ramdom 

for x in objects:
	print(x)

if "daivd" in objects:
	print("Yes, It has david")

objects.add("Guna1")
objects.update(["Guna", "Rakulan", "Gunarakulan"])

print(objects)
print(len(objects))

objects.remove("Rakulan")
objects.discard("Guna1")

objects.pop() #
objects.clear()

print(objects)