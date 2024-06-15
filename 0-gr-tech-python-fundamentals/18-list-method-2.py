# copy
# merge / extend
# count
# index

# copy
objects = ["car", "dog", "phone", "cup", "laptop"]
objects2 = objects.copy()
objects.remove("dog")
print(objects)
print(objects2)


# merge
list1 = ["dog", "cat", "phone"]
list2 = ["laptop", "apple", "orange","laptop"]

#totalList = list1 + list2
list1.extend(list2)

#print(list1)

print(list1.count("dog"))

print(list1.index("orange"))
