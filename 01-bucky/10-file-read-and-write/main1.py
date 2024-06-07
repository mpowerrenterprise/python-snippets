fw=open("sam.txt",'w')
fw.write("Hello My name is guna \n")
fw.write("I work as an computer engineer")
fw.close()


fr=open("sam.txt","r")
text=fr.read()
print(text)
fr.close()