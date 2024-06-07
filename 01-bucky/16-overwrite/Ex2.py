class Parent():
	def print_First_name(self):
		print("Guna")

class child(Parent): # child inherites from the Prarent
	def print_last_name(self):
		print("Rakulan")

	def print_First_name(self): #This is overwrite
		print("Gta")

guna = child()
guna.print_First_name();
guna.print_last_name();