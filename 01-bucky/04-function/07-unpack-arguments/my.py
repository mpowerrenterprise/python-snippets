def helthCalculator(age,apple_ate,smoke):
	answer=(100-age)+(apple_ate*3.5)-(smoke*2)
	print(answer)


guna_data=[21,20,0]
joker_data=[21,10,0]

helthCalculator(guna_data[0],guna_data[1],guna_data[2])
helthCalculator(*joker_data) # This is called argument unpacking.

