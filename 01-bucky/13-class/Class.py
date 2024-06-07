class Ememy:
	life = 3

	def attck(self):   #"self" keyword we can access the attributes and methods of the class in python.
		print("Ouch!..")
		self.life-=1   # we cannot directly use the name of variable like life.

	def checkLife(self):

		if self.life <= 0: 
			print("I am dead")

		else:
			print("The life left is " + str(self.life))


ememy1 = Ememy() #object
ememy2 = Ememy() #object

ememy1.attck()
ememy1.checkLife()

ememy2.checkLife()


#Objects are the instance of a class.
#ememy1 and ememy2 are the diffrent objects.



