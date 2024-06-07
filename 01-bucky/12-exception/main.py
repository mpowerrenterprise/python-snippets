while True:
	try:
		number=int(input("What is your favorite number ?\n"))
		print(18/number)
		break
	
	except ValueError:     # in python we can defind the Error MSG and give specific solution for this.
						   # This is the ValueError.
		print ("Make sure and enter the right value")

	except ZeroDivisionError: #This is for ZeroDivisionError Error. It only expect for that specific Error.
		print("Do not pick zero")

	except:                   #This works for everything. If any Error finds in this application, it will thorw the exception.
		print("Someting went wrong")
	finally:                 #No matter what, It will work.
		print("I work whatever happens")