person1 = {"name":"david", "age":66, "job":"Web Developer", "From":"USA"}



# Check If value exist
# len
# add
# pop("name")
# popitem()
# del person1['name']
# del person1
# clear()


if "name" in person1.keys():
	print("Yes, It exists")

if "david" in person1.values():
	print("Yes, It exists")


print(len(person1))


person1["new_info"] = "This is a new value"

person1.popitem()
print(person1)



person1.popitem() # Removes last item


# Delete elements from dictionary 
del person1['name']
person1.popitem()
person1.popitem() 

#Remove the dictionary
person1.clear()

print(person1)