'''

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)




file = open("sample-text.txt", "rt")
file.write("Hello")
#print(file.readlines()[2])
file.close()





file = open("sample-text.txt", "at")
file.write("\n The third content")

file.close()

'''




file = open("sample-text-2.txt", "xt")
file.write("this is new text")

file.close()