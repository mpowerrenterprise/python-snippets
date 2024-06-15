#append()
#insert()
#remove()
#pop() del name[0]
#clear()
#reverse()

# append
objects = ["car", "bike", "phone", "computer", "laptop"]
objects.append("dog")
print(objects)


#insert
objects.insert(1, "headphone")
print(objects)

#remove
objects.remove("headphone")
objects.remove("dog")
objects.pop(1)
del objects[0]
print(objects)

#reverse
objects.reverse()
print(objects)

#clear
objects.clear()
print(objects)