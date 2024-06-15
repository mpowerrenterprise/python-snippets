# >= 35 = S
# >= 45 = C
# >= 65 = B
# >= 75 = A
# >= 90 = A+

subject_name = input("Please enter a subject name? ")
marks = int(input(f"Please enter your marks in {subject_name}? "))

if marks >= 0 and marks < 35:
	print("You failed in the exam")

elif marks >= 35 and marks < 45:
	print(f"You have recived S in {subject_name}")

elif marks >= 45 and marks < 65:
	print(f"You have recived C in {subject_name}")

elif marks >= 65 and marks < 75:
	print(f"You have recived B in {subject_name}")

elif marks >= 75 and marks < 90:
	print(f"You have recived A in {subject_name}")

elif marks >= 90 and marks <= 100:
	print(f"You have recived A+ in {subject_name}")
else:
	print("Sorry, I could not process this")