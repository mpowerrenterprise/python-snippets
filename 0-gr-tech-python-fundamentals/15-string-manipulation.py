# 00 String as list
# 01 Looping string
# 02 Slicing
# 03 Length
# 04 strip()
# 05 lower()
# 06 upper()
# 07 replace("Guna", "Kuna")
# 08 split("|")
# 09 Check string "free" in txt
# 10 String Concatenation f string
# 11 String Concatenation Format


#list
name = "This is a simple text"
print(name[1])


#Looping

for c in name:
	if "s" == c:
		print("S found")

# Slicing
print(name[5:]) 
print(name[5:7])

#upper lower()
data = input("Enter some data? ")
print(data.upper())
print(data.lower())



#replace

newValue = input("Enter your name? ")
print(newValue.replace("My name is", "I am"))


#Split 
textData = "apple | orange | dog | cat"
textData = textData.split("|")
print(textData[1])


userData = input("Enter something: ")

if "kill" in userData:
	print("Bad sentance")
else:
	print("good sentance")


#String Concatenation f string

data1 = "hello"
data2 = "bye"

print(f"{data1} {data2}")

print("{} {}".format(data1, data2))

